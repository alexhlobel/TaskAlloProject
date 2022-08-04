from rest_framework import viewsets, response
from .serializers import TaskSerializer
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    """Список задач"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


