from rest_framework import serializers
from .models import Comment, ImageComment


class ImageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComment
        fields = '__all__'


class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
