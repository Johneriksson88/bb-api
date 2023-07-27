from rest_framework import permissions

"""
Returns a boolean to determine whether user has read access by default
and if not checks if user is the owner of the object.
Create permission to check if the user is the owner.
"""
class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user