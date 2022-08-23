from rest_framework import viewsets
from rest_framework.response import Response

from TaskAlloProject.permissions import IsManagerOrReadOnly
from .serializers import TaskSerializer, ImageTaskSerializer
from .models import Task, ImageTask


class TaskViewSet(viewsets.ModelViewSet):
    """Список задач"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsManagerOrReadOnly]

    def list(self, request, *args, **kwargs):
        prefiltered_queryset = self.queryset

        if request.user.role == 'worker':
            prefiltered_queryset = self.queryset.filter(team_id=request.user.team.id)

        elif request.user.role == 'manager':
            prefiltered_queryset = self.queryset.filter(team__manager=request.user.id)

        queryset = self.filter_queryset(prefiltered_queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ImageTaskViewSet(viewsets.ModelViewSet):
    """Список изображений заданий"""
    serializer_class = ImageTaskSerializer
    queryset = ImageTask.objects.all()
    permission_classes = [IsManagerOrReadOnly]
