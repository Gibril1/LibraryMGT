from rest_framework.permissions import BasePermission,  SAFE_METHODS

class LibrarianPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Librarian'

class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Student'
    

class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user





