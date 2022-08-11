from django.urls import path, include
from .views import TaskViewSet, ImageTaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task', TaskViewSet, basename='task')
router.register(r'image', ImageTaskViewSet, basename='task_image')

urlpatterns = router.urls
