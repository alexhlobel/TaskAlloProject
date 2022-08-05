from rest_framework import viewsets, response
from .serializers import TaskSerializer, ImageTaskSerializer
from .models import Task, ImageTask
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    """Список задач"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ImageTaskViewSet(viewsets.ModelViewSet):
    """Список изображений заданий"""
    serializer_class = ImageTaskSerializer
    queryset = ImageTask.objects.all()
