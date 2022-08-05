from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'id', 'first_name',
                  'last_name', 'date_joined', 'password']


class TeamSerializer(serializers.ModelSerializer):
    worker = UserSerializer(many=False)
    manager = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'worker', 'manager']
