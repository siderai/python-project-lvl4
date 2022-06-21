from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a task
        return obj.author == request.user


class IsCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only current user can edit himself
        return obj == request.user
