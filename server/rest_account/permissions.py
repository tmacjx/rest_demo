# coding=utf-8
from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'LIST')


class UserPermission(BasePermission):
    def check_object_permissions(self, request, obj):
        pass

    def check_permissions(self, request):
        pass


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user.is_authenticated() and request.user.is_staff
        )
    # retrieve update partial_update destroy时
    # modelviewset默认会调用get_object来进行object permission权限检查

    def check_object_permissions(self, request, obj):
        return True