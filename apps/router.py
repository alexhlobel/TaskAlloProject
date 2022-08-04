from django.urls import path, include


routes = [
    path('employees/', include('apps.Employees.urls')),
    path('tasks/', include('apps.Task.urls')),
]