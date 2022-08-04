from rest_framework import viewsets, response
from .serializers import ConnectSerializer
from .models import Comment

class CommentViewSet(viewsets.ModelViewSet):
    """Список всех коментов"""
    serializer_class = ConnectSerializer
    queryset = Comment.objects.all()
