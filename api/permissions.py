from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
   def has_permission(self, request, view):
       if request.method in permissions.SAFE_METHODS or not request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
           return True

       return bool(request.user and request.user.is_staff)