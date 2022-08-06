from rest_framework import serializers
from .models import Task, ImageTask
from apps.Employees.serializers import UserSerializer, TeamSerializer


class ImageTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)
    creator = UserSerializer(many=False)

    class Meta:
        model = Task
        fields = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
                  'creator', 'status_task', 'deadline', 'image_task']
