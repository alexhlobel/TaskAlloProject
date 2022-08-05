from rest_framework import serializers
from .models import Task, ImageTask


class ImageTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
        #           'creator', 'status_task', 'deadline']
