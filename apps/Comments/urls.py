from django.urls import path
from .views import CommentViewSet, ImageCommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('comment', CommentViewSet, basename='comment')
router.register('image', ImageCommentViewSet, basename='image')


urlpatterns = router.urls
