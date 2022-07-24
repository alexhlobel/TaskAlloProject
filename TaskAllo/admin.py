from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.safestring import mark_safe

# print(User.__dict__.keys())
# print(models.ImageField.__dict__.keys())
'''
    date_hierarchy = 'created_at'
    list_display = ('title', 'created_at', 'preview_content', 'author', 'preview_image')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'image')
        }),
        ('Дополнительная информация', {
            'classes': ('collapse',),
            'fields': ('created_at',),
        }),
    )

    @staticmethod
    def preview_image(obj):
        if obj.image:
            print(obj.image.url)
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
            # return mark_safe(f'<img src="../media/ImagePost/pikachu.png" width="100" />')

    @staticmethod
    def preview_content(obj):
        return obj.content[:30]
'''


class NameAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name']
    search_fields = ['name']


class StatusEmployeeAdmin(NameAdmin):
    pass


class TeamAdmin(NameAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


class WorkerAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    ordering = ['username']
    list_display = ['username', 'id', 'status_emp', 'team', 'last_login', 'is_superuser',  'first_name', 'last_name',
                    'email', 'is_staff', 'is_active', 'date_joined', ]
    list_filter = ['status_emp', 'team']
    search_fields = ['username', 'email']
    readonly_fields = ('date_joined', 'last_login', 'id')
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'id', 'status_emp', 'team', 'first_name',
                       'last_name', 'date_joined', 'password', )
        }),
        ('Additional parameters', {
            'classes': ('collapse',),
            'fields': ('last_login', 'is_superuser', 'is_staff', 'is_active'),
        }),
    )


class ManagerAdmin(admin.ModelAdmin):

    @staticmethod
    def get_teams(obj):
        return ",\n".join([str(p) for p in obj.team.all()])

        # Когда потом в get_teams передается obj? Почему это срабатывает?

    date_hierarchy = 'date_joined'
    ordering = ['username']
    list_display = ['username', 'id', 'status_emp', 'get_teams', 'last_login',
                    'is_superuser',  'first_name', 'last_name', 'email',
                    'is_staff', 'is_active', 'date_joined', ]
    list_filter = ['status_emp', 'team']
    search_fields = ['username', 'email']
    readonly_fields = ('date_joined', 'last_login', 'id', 'team')
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'id', 'status_emp', 'team', 'first_name',
                       'last_name', 'date_joined', 'password', )
        }),
        ('Additional parameters', {
            'classes': ('collapse',),
            'fields': ('last_login', 'is_superuser', 'is_staff', 'is_active'),
        }),
    )


class ManagershipAdmin(admin.ModelAdmin):
    fields = ['manager', 'team', 'id']
    ordering = ['manager', 'id']
    list_display = ['manager', 'team', 'id']
    search_fields = ['name', 'team']
    list_filter = ['manager', 'team']
    readonly_fields = ['id']


class AdminAdmin(ManagerAdmin):
    pass


class StatusTaskAdmin(NameAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    ordering = ['name']
    list_display = ['name', 'id', 'description', 'team', 'created_at', 'updated_at', 'image_source',
                    'author', 'status_task', 'deadline', ]
    list_filter = ['team', 'author']
    search_fields = ['username', 'email']
    readonly_fields = ('created_at', 'updated_at', 'id', 'connection')
    fieldsets = (
        (None, {
            'fields': ['name', 'id', 'description', 'team', 'created_at', 'updated_at', 'image_source',
                       'author', 'status_task', 'deadline', 'connection']
        }),
        ('Additional parameters', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )


class ConnectionAdmin(admin.ModelAdmin):
    fields = ['id', 'task_1', 'task_2', ]
    ordering = ['task_1', ]
    list_display = ['__str__', ]
    search_fields = ['task_1', 'task_2', ]
    readonly_fields = ('id', )


class CommentAdmin(admin.ModelAdmin):

    @staticmethod
    def preview_content(obj):
        return obj.content[:30]

    # @staticmethod
    # def preview_image(obj):
    #     if obj.image:
    #         return mark_safe(f'<img src="{obj.image.url}" width="100" />')

    fields = ['id', 'owner', 'task', 'created_at', 'content', 'image_source']
    date_hierarchy = 'created_at'
    ordering = ['created_at', ]
    list_filter = ['owner', ]
    list_display = ['id', 'owner', 'task', 'created_at', 'preview_content', 'image_source']
    search_fields = ['owner', 'content', ]
    readonly_fields = ('id', 'created_at', )


class ImageAdmin(admin.ModelAdmin):
    @staticmethod
    def image_name(obj):
        return obj.image.name

    fields = ['id', 'image', 'source', ]
    ordering = ['id', ]
    list_display = ['__str__', 'source', ]
    search_fields = ['image', 'source', ]
    readonly_fields = ('id', )


class ImageSourceAdmin(admin.ModelAdmin):
    fields = ['id']
    ordering = ['id', ]
    list_display = ['__str__', 'id']
    search_fields = ['id', ]
    readonly_fields = ('id', )


admin.site.register(StatusEmployee, StatusEmployeeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Managership, ManagershipAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(StatusTask, StatusTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageSource, ImageSourceAdmin)
