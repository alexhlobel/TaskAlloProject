from rest_framework import serializers
from .models import Task, ImageTask


class ImageTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
                  'image_task', 'creator', 'status_task', 'deadline', 'image_task', 'assigned_task', 'comment_task']
