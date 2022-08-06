from django.urls import path
from .views import CommentViewSet, ImageCommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'image', ImageCommentViewSet, basename='comment_image')


urlpatterns = router.urls
