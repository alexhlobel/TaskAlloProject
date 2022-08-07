from rest_framework import serializers
from .models import Comment, ImageComment
from apps.Employees.serializers import UserSerializer
from apps.Task.serializers import TaskSerializer


class ImageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer(many=False)
    # task = TaskSerializer(many=False)

    class Meta:
        model = Comment
        fields = ['author', 'created_at', 'content', 'image_comment', 'task']
