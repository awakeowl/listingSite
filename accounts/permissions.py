from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return perform_check(request, "ADMIN")


class IsEditor(permissions.BasePermission):

    def has_permission(self, request, view):
        return perform_check(request, "EDITOR")


class IsViewer(permissions.BasePermission):

    def has_permission(self, request, view):
        return perform_check(request, "VIEWER")


def perform_check(request, role):
    return request.user.role == role
