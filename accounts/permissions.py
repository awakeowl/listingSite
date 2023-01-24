from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return perform_check(request, "ADMIN")


def perform_check(request, role):
    return request.user.role == role
