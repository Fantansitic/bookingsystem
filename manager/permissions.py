from rest_framework import permissions

class LoginRequire(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTH_TOKEN',None)
        if token is None:
            return False
        return True