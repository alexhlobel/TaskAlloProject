from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
SAFE_POST_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')


class IsManagerOrReadOnly(BasePermission):
    """
    Allows full access only to managers and admins, otherwise - reading only.
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return bool(request.method in SAFE_METHODS or request.user.role in ['admin', 'manager'])
        return False


class IsAdminOrReadOnly(BasePermission):
    """
    Allows access only to manager.
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return bool(request.method in SAFE_METHODS or request.user.role == 'admin')
        return False


class IsAdminOrManagerWithoutDeleteOrReadOnly(BasePermission):
    """
    Allows access only to manager.
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return bool(request.method in SAFE_METHODS
                        or (request.method != 'DELETE' and request.user.role == 'manager')
                        or request.user.role == 'admin')
        return False


class IsManagerOrReadAndPostOnly(BasePermission):
    """
    Allows full access only to managers and admins, otherwise - reading only.
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return bool(request.method in SAFE_POST_METHODS or request.user.role in ['admin', 'manager'])
        return False
