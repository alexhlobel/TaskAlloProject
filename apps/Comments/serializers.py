from rest_framework import serializers
from .models import Comment, ImageComment


class ImageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'id', 'created_at', 'content', 'image_comment', 'task']
