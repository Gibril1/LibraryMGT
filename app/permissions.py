from rest_framework.permissions import BasePermission,  SAFE_METHODS

class LibrarianPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Librarian'

class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Student'





