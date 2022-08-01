from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'id', 'first_name',
                  'last_name', 'date_joined', 'password', 'RolesChoice']


# class TeamSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Team
#         fields = ['id', 'name']
#
#
# class WorkerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Worker
#         fields = ['username', 'email', 'id', 'status_emp', 'team'
#                                                            'first_name', 'last_name', 'date_joined', 'password', ]
#
#
# class ManagerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Manager
#         fields = ['username', 'email', 'id', 'status_emp', 'team'
#                                                            'first_name', 'last_name', 'date_joined', 'password', ]
#
#
# class ManagershipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Managership
#         fields = ['id', 'team', 'manager']
#
#
# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = ['username', 'email', 'id', 'status_emp', 'team'
#                                                            'first_name', 'last_name', 'date_joined', 'password', ]
#
#
# class ImageSourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImageSource
#         fields = ['id', ]
#
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['name', 'id', 'description', 'team', 'created_at', 'updated_at',
#                   'image', 'author', 'status_task', 'deadline', 'connection']
#
#
# class ConnectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Connection
#         fields = '__all__'
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'
