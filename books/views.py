from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .models import Book
from library.models import Library
from .serializers import BookSerializers
from app.permissions import LibrarianPermission


# Create your views here.
class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.librarian.user == request.user


class BookCreateView(APIView):
    permission_classes = [IsAuthenticated, LibrarianPermission]
    def get_library(self, pk):
        try:
            return Library.objects.get(id=pk)
        except Library.DoesNotExist:
            raise Http404
        
    def post(self, request, pk):
        library = self.get_library(pk)
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(library=library)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookView(APIView):
    permission_classes = [IsAuthenticated]
    def get_library(self, pk):
        try:
            return Library.objects.get(id=pk)
        except Library.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        library = self.get_library(pk)
        books = Book.objects.filter(library=library)
        serializer = BookSerializers(books)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
