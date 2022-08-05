from django.contrib import admin
from .models import Comment, ImageComment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageComment)
class ImageCommentAdmin(admin.ModelAdmin):
    pass
