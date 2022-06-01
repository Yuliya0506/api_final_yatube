from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthorChangeObject(BasePermission):
    message = 'Только автор может изменить объект.'
    code = status.HTTP_403_FORBIDDEN

    def has_object_permission(self, request, view, obj):
        permission = (
            request.user == obj.author or request.method in SAFE_METHODS
        )
        return permission
