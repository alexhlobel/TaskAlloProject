from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Allows access only to managers and admins.
    """

    def has_permission(self, request, view):
        print('I am ismanager')
        print(request.user.is_superuser)
        if hasattr(request.user, 'role'):
            return bool(request.user.role in ['admin', 'manager'])
        return False


class IsAdmin(BasePermission):
    """
    Allows access only to manager.
    """

    def has_permission(self, request, view):
        print('I am isadmin')
        if hasattr(request.user, 'role'):
            return bool(request.user and request.user.role == 'admin')
        return False
