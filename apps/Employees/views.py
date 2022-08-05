import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.Employees.models import CustomUser, Team
from apps.Employees.serializers import UserSerializer, TeamSerializer


class UsersViewSet(ModelViewSet):
    """Список всех пользователей"""
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


class TeamViewSet(ModelViewSet):
    """Список команд"""
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAdminUser]
