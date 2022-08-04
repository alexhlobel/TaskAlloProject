from django.urls import path
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('comment/', CommentViewSet, basename='comment')


urlpatterns = router.urls
