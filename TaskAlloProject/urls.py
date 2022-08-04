from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.router import routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routes)),
]
