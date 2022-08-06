from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'id', 'first_name',
                  'last_name', 'date_joined', 'password', 'slug']
        lookup_field = "slug"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        print('YA UPDATE')
        return super(UserSerializer, self).update(instance, validated_data)


class TeamSerializer(serializers.ModelSerializer):
    manager = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'manager']
