from django.urls import path
from .views import TaskViewSet, ImageTaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task', TaskViewSet, basename='task')
router.register(r'image', ImageTaskViewSet, basename='image')

urlpatterns = router.urls
