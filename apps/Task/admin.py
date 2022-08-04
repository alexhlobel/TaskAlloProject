from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
    # @staticmethod
    # def preview_image(obj):
    #     try:
    #         image_task = ImageTask.objects.filter(source_id=obj.image_task.id)
    #         images_str = '<br><br>'.join([f'<img src="{element.image.url}" width="100" />' for element in image_task])
    #         images = mark_safe(images_str)
    #         return images
    #     except AttributeError:
    #         return 'No image'
    #
    # date_hierarchy = 'created_at'
    # ordering = ['name']
    # list_display = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
    #                 'author', 'status_task', 'comment_task', 'deadline']
    # list_filter = ['team', 'author']
    # search_fields = ['username', 'email']
    # readonly_fields = ('created_at', 'updated_at', 'id', 'comment_task')
    # fieldsets = (
    #     (None, {
    #         'fields': ['name', 'id', 'description', 'team', 'created_at', 'updated_at', 'image_task',
    #                    'author', 'status_task', 'comment_task', 'deadline']
    #     }),
    #     ('Additional parameters', {
    #         'classes': ('collapse',),
    #         'fields': (),
    #     }),
    # )