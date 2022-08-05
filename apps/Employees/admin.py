from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password


csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def get_urls(self):
        return [
                   path(
                       "<id>/password/",
                       self.admin_site.admin_view(self.user_change_password),
                       name="auth_user_password_change",
                   ),
               ] + super().get_urls()

    def lookup_allowed(self, lookup, value):
        # Don't allow lookups involving passwords.
        return not lookup.startswith("password") and super().lookup_allowed(
            lookup, value
        )

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url="", extra_context=None):
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)

    def _add_view(self, request, form_url="", extra_context=None):
        # It's an error for a user to have add permission but NOT change
        # permission for users. If we allowed such users to add users, they
        # could create superusers, which would mean they would essentially have
        # the permission to change users. To avoid the problem entirely, we
        # disallow users from adding users if they don't have change
        # permission.
        if not self.has_change_permission(request):
            if self.has_add_permission(request) and settings.DEBUG:
                # Raise Http404 in debug mode so that the user gets a helpful
                # error message.
                raise Http404(
                    'Your user does not have the "Change user" permission. In '
                    "order to add users, Django requires that your user "
                    'account have both the "Add user" and "Change user" '
                    "permissions set."
                )
            raise PermissionDenied
        if extra_context is None:
            extra_context = {}
        username_field = self.model._meta.get_field(self.model.USERNAME_FIELD)
        defaults = {
            "auto_populated_fields": (),
            "username_help_text": username_field.help_text,
        }
        extra_context.update(defaults)
        return super().add_view(request, form_url, extra_context)

    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=""):
        user = self.get_object(request, unquote(id))
        if not self.has_change_permission(request, user):
            raise PermissionDenied
        if user is None:
            raise Http404(
                _("%(name)s object with primary key %(key)r does not exist.")
                % {
                    "name": self.model._meta.verbose_name,
                    "key": escape(id),
                }
            )
        if request.method == "POST":
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = gettext("Password changed successfully.")
                messages.success(request, msg)
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect(
                    reverse(
                        "%s:%s_%s_change"
                        % (
                            self.admin_site.name,
                            user._meta.app_label,
                            user._meta.model_name,
                        ),
                        args=(user.pk,),
                    )
                )
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {"fields": list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            "title": _("Change password: %s") % escape(user.get_username()),
            "adminForm": adminForm,
            "form_url": form_url,
            "form": form,
            "is_popup": (IS_POPUP_VAR in request.POST or IS_POPUP_VAR in request.GET),
            "is_popup_var": IS_POPUP_VAR,
            "add": True,
            "change": False,
            "has_delete_permission": False,
            "has_change_permission": True,
            "has_absolute_url": False,
            "opts": self.model._meta,
            "original": user,
            "save_as": False,
            "show_save": True,
            **self.admin_site.each_context(request),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.change_user_password_template
            or "admin/auth/user/change_password.html",
            context,
        )

    def response_add(self, request, obj, post_url_continue=None):
        """
        Determine the HttpResponse for the add_view stage. It mostly defers to
        its superclass implementation but is customized because the User model
        has a slightly different workflow.
        """
        # We should allow further modification of the user just added i.e. the
        # 'Save' button should behave like the 'Save and continue editing'
        # button except in two scenarios:
        # * The user has pressed the 'Save and add another' button
        # * We are adding a user in a popup
        if "_addanother" not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST["_continue"] = 1
        return super().response_add(request, obj, post_url_continue)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


# @admin.register(ImageComment)
# class ImageCommentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ImageTask)
# class ImageTaskAdmin(admin.ModelAdmin):
#     list_display = ['id', 'image_task']
#
#
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     pass
#     # @staticmethod
#     # def preview_image(obj):
#     #     try:
#     #         image_task = ImageTask.objects.filter(source_id=obj.image_task.id)
#     #         images_str = '<br><br>'.join([f'<img src="{element.image.url}" width="100" />' for element in image_task])
#     #         images = mark_safe(images_str)
#     #         return images
#     #     except AttributeError:
#     #         return 'No image'
#     #
#     # date_hierarchy = 'created_at'
#     # ordering = ['name']
#     # list_display = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
#     #                 'author', 'status_task', 'comment_task', 'deadline']
#     # list_filter = ['team', 'author']
#     # search_fields = ['username', 'email']
#     # readonly_fields = ('created_at', 'updated_at', 'id', 'comment_task')
#     # fieldsets = (
#     #     (None, {
#     #         'fields': ['name', 'id', 'description', 'team', 'created_at', 'updated_at', 'image_task',
#     #                    'author', 'status_task', 'comment_task', 'deadline']
#     #     }),
#     #     ('Additional parameters', {
#     #         'classes': ('collapse',),
#     #         'fields': (),
#     #     }),
#     # )
#
# # # Как захэшировать пароль в админке без UserAdmin?
# #
# #
# # class NameAdmin(admin.ModelAdmin):
# #     ordering = ['name']
# #     list_display = ['name']
# #     search_fields = ['name']
# #
# #
# # class StatusEmployeeAdmin(NameAdmin):
# #     pass
# #
# #
# # class TeamAdmin(NameAdmin):
# #     pass
# #
# #
# # class EmployeeAdmin(admin.ModelAdmin):
# #     date_hierarchy = 'date_joined'
# #     ordering = ['username']
# #     list_display = ['username', 'id', 'status_emp', 'last_login', 'is_superuser', 'first_name', 'last_name',
# #                     'email', 'is_staff', 'is_active', 'date_joined', ]
# #     list_filter = ['status_emp', ]
# #     search_fields = ['username', 'email']
# #     readonly_fields = ('date_joined', 'last_login', 'id')
# #     fieldsets = (
# #         (None, {
# #             'fields': ('username', 'email', 'id', 'status_emp', 'first_name',
# #                        'last_name', 'date_joined', 'password',)
# #         }),
# #         ('Additional parameters', {
# #             'classes': ('collapse',),
# #             'fields': ('last_login', 'is_superuser', 'is_staff', 'is_active'),
# #         }),
# #     )
# #
# #
# # class WorkerAdmin(admin.ModelAdmin):
# #     date_hierarchy = 'date_joined'
# #     ordering = ['username']
# #     list_display = ['username', 'id', 'status_emp', 'team', 'last_login', 'is_superuser', 'first_name', 'last_name',
# #                     'email', 'is_staff', 'is_active', 'date_joined', ]
# #     list_filter = ['status_emp', 'team']
# #     search_fields = ['username', 'email']
# #     readonly_fields = ('date_joined', 'last_login', 'id')
# #     fieldsets = (
# #         (None, {
# #             'fields': ('username', 'email', 'id', 'status_emp', 'team', 'first_name',
# #                        'last_name', 'date_joined', 'password',)
# #         }),
# #         ('Additional parameters', {
# #             'classes': ('collapse',),
# #             'fields': ('last_login', 'is_superuser', 'is_staff', 'is_active'),
# #         }),
# #     )
# #
# #
# # class ManagerAdmin(admin.ModelAdmin):
# #
# #     @staticmethod
# #     def get_teams(obj):
# #         return ",\n".join([str(p) for p in obj.team.all()])
# #
# #         # Когда потом в get_teams передается obj? Почему это срабатывает?
# #
# #     date_hierarchy = 'date_joined'
# #     ordering = ['username']
# #     list_display = ['username', 'id', 'status_emp', 'get_teams', 'last_login',
# #                     'is_superuser', 'first_name', 'last_name', 'email',
# #                     'is_staff', 'is_active', 'date_joined', ]
# #     list_filter = ['status_emp', 'team']
# #     search_fields = ['username', 'email']
# #     readonly_fields = ('date_joined', 'last_login', 'id', 'team')
# #     fieldsets = (
# #         (None, {
# #             'fields': ('username', 'email', 'id', 'status_emp', 'team', 'first_name',
# #                        'last_name', 'date_joined', 'password',)
# #         }),
# #         ('Additional parameters', {
# #             'classes': ('collapse',),
# #             'fields': ('last_login', 'is_superuser', 'is_staff', 'is_active'),
# #         }),
# #     )
# #
# #
# # class ManagershipAdmin(admin.ModelAdmin):
# #     fields = ['manager', 'team', 'id']
# #     ordering = ['manager', 'id']
# #     list_display = ['manager', 'team', 'id']
# #     search_fields = ['name', 'team']
# #     list_filter = ['manager', 'team']
# #     readonly_fields = ['id']
# #
# #
# # class AdminAdmin(ManagerAdmin):
# #     pass
# #
# #
# # class StatusTaskAdmin(NameAdmin):
# #     pass
# #
# #
# # class TaskAdmin(admin.ModelAdmin):
# #
# #     @staticmethod
# #     def preview_image(obj):
# #         try:
# #             image_query = Image.objects.filter(source_id=obj.image_source.id)
# #             images_str = '<br><br>'.join([f'<img src="{element.image.url}" width="100" />' for element in image_query])
# #             images = mark_safe(images_str)
# #             return images
# #         except AttributeError:
# #             return 'No image'
# #
# #     date_hierarchy = 'created_at'
# #     ordering = ['name']
# #     list_display = ['name', 'id', 'description', 'team', 'created_at', 'updated_at', 'image_source',
# #                     'preview_image', 'author', 'status_task', 'deadline', ]
# #     list_filter = ['team', 'author']
# #     search_fields = ['username', 'email']
# #     readonly_fields = ('created_at', 'updated_at', 'id', 'connection')
# #     fieldsets = (
# #         (None, {
# #             'fields': ['name', 'id', 'description', 'team', 'created_at', 'updated_at', 'image_source',
# #                        'author', 'status_task', 'deadline', 'connection']
# #         }),
# #         ('Additional parameters', {
# #             'classes': ('collapse',),
# #             'fields': (),
# #         }),
# #     )
# #
# #
# # class ConnectionAdmin(admin.ModelAdmin):
# #     fields = ['id', 'task_1', 'task_2', ]
# #     ordering = ['task_1', ]
# #     list_display = ['__str__', ]
# #     search_fields = ['task_1', 'task_2', ]
# #     readonly_fields = ('id',)
# #
# #
# # class CommentAdmin(admin.ModelAdmin):
# #
# #     @staticmethod
# #     def preview_content(obj):
# #         return obj.content[:30]
# #
# #     @staticmethod
# #     def preview_image(obj):
# #         try:
# #             image_query = Image.objects.filter(source_id=obj.image_source.id)
# #             images_str = '<br><br>'.join([f'<img src="{element.image.url}" width="100" />' for element in image_query])
# #             images = mark_safe(images_str)
# #             return images
# #         except AttributeError:
# #             return 'No image'
# #
# #     fields = ['id', 'owner', 'task', 'created_at', 'content', 'image_source']
# #     date_hierarchy = 'created_at'
# #     ordering = ['created_at', ]
# #     list_filter = ['owner', ]
# #     list_display = ['preview_content', 'id', 'owner', 'task', 'created_at', 'preview_image', 'image_source']
# #     search_fields = ['owner', 'content', ]
# #     readonly_fields = ('id', 'created_at',)
# #
# #
# # class ImageAdmin(admin.ModelAdmin):
# #     @staticmethod
# #     def image_name(obj):
# #         return obj.image.name
# #
# #     @staticmethod
# #     def preview_image(obj):
# #         if obj.image:
# #             return mark_safe(f'<img src="{obj.image.url}" width="100" />')
# #
# #     fields = ['id', 'image', 'source', ]
# #     ordering = ['id', ]
# #     list_display = ['__str__', 'source', 'preview_image']
# #     search_fields = ['image', 'source', ]
# #     readonly_fields = ('id',)
# #
# #
# # class ImageSourceAdmin(admin.ModelAdmin):
# #
# #     @staticmethod
# #     def preview_image(obj):
# #         try:
# #             image_query = Image.objects.filter(source_id=obj.id)
# #             images_str = '<br><br>'.join([f'<img src="{element.image.url}" width="100" />' for element in image_query])
# #             images = mark_safe(images_str)
# #             return images
# #         except AttributeError:
# #             return 'No image'
# #
# #     fields = ['id']
# #     ordering = ['id', ]
# #     list_display = ['__str__', 'id', 'preview_image']
# #     search_fields = ['id', ]
# #     readonly_fields = ('id',)
# #
# #
# # admin.site.register(Team, TeamAdmin)
# # admin.site.register(CustomUser, UserAdmin)
# # admin.site.register(Worker, WorkerAdmin)
# # admin.site.register(Manager, ManagerAdmin)
# # admin.site.register(Managership, ManagershipAdmin)
# admin.site.register(Admin, AdminAdmin)
# # admin.site.register(Task, TaskAdmin)
# # admin.site.register(Comment, CommentAdmin)
# # admin.site.register(Image, ImageAdmin)
# # admin.site.register(ImageSource, ImageSourceAdmin)
