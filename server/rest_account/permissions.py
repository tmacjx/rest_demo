from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def check_object_permissions(self, request, obj):
        pass

    def check_permissions(self, request):
        pass