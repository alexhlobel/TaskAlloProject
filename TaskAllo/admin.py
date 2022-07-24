from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import *

print(User.__dict__.keys())
print(models.ImageField.__dict__.keys())
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
    list_display = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
                    'author', 'status_task', 'deadline', ]
    list_filter = ['team', 'author']
    search_fields = ['username', 'email']
    readonly_fields = ('created_at', 'updated_at', 'id', 'connection')
    fieldsets = (
        (None, {
            'fields': ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
                       'author', 'status_task', 'deadline', 'connection']
        }),
        ('Additional parameters', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )


admin.site.register(StatusEmployee, StatusEmployeeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Managership, ManagershipAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(StatusTask, StatusTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(ImageSource)
