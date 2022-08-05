from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


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
