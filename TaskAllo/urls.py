from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='Tasks')
router.register(r'teams', TeamViewSet, basename='Teams')
router.register(r'users', UsersViewSet, basename='Users')

urlpatterns = router.urls
