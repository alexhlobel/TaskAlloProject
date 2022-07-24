from rest_framework import serializers
from .models import *


class StatusEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusEmployee
        fields = ['name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['status_emp']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['team']


class ManagershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managership
        fields = ['team', 'manager']


# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = ['name']


class StatusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTask
        fields = ['name']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'team', 'created_at', 'updated_at', 'image', 'author', 'status_task',
                  'deadline', 'connection']
