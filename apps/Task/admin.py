from django.contrib import admin
from .models import Task, ImageTask


@admin.register(ImageTask)
class ImageTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
              'creator', 'status_task', 'deadline', 'image_task', 'tasks_connections']
    readonly_fields = ('created_at', 'updated_at', 'id')
