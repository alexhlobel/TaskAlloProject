from django.urls import path, include
from apps.Employees.views import UsersViewSet, TeamViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'teams', TeamViewSet, basename='Teams')
router.register(r'users', UsersViewSet, basename='Users')

urlpatterns = router.urls
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]