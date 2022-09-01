from rest_framework import permissions


class GetOrAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.role == 'admin'

    # def has_object_permission(self, request, view, obj):
    #     if request.method == 'GET':
    #         return False
    #     return super().has_object_permission(request, view, obj)


class ObjNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
