from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее редактировать объект
    только владельцам.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
