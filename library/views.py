from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LibrarySerializer
from .models import Library
from users.models import LibrarianProfile
from app.permissions import LibrarianPermission

class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.librarian.user == request.user


# Create your views here.
class LibraryCreateView(APIView):
    permission_classes = [IsAuthenticated, LibrarianPermission]
    def get_librarian(self, user):
        try:
            return LibrarianProfile.objects.get(user=user)
        except:
            raise Http404
    
    def post(self, request):
        librarian = self.get_librarian(request.user)
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(librarian=librarian)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LibraryView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryDetailsView(UpdateAPIView):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class GetLibraryDetailsView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
