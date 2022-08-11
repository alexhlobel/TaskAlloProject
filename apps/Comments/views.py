from rest_framework import viewsets, response
from .serializers import CommentSerializer, ImageCommentSerializer
from .models import Comment, ImageComment
from TaskAlloProject.permissions import IsManagerOrReadAndPostOnly


class CommentViewSet(viewsets.ModelViewSet):
    """Список всех коментов"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsManagerOrReadAndPostOnly]


class ImageCommentViewSet(viewsets.ModelViewSet):
    """Список всех изображений для комментов"""
    serializer_class = ImageCommentSerializer
    queryset = ImageComment.objects.all()
    permission_classes = [IsManagerOrReadAndPostOnly]
