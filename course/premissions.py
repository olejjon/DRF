from rest_framework import permissions
from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user