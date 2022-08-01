from rest_framework import viewsets, response
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


# class TaskViewSet(viewsets.ModelViewSet):
#     """Список задач"""
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()
#
#
# class TeamViewSet(viewsets.ModelViewSet):
#     """Список команд"""
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()
#
#
class UsersViewSet(viewsets.ModelViewSet):
    """Список всех пользователей"""
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
