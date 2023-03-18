from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .models import Book, BorrowBook
from library.models import Library
from users.models import StudentProfile, LibrarianProfile
from .serializers import BookSerializers, BorrowBookSerializers
from app.permissions import LibrarianPermission, StudentPermission


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
    permission_classes = [IsAuthenticated, StudentPermission]
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

class BorrowBook(APIView):
    permission_classes = [IsAuthenticated]
    def get_book(self, pk):
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404
        
    def get_student_profile(self, user):
        try:
            return StudentProfile.objects.get(user=user)
        except StudentProfile.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        book = self.get_book(pk)
        student = self.get_student_profile(request.user)
        borrowed_book = BorrowBook(
            book = book,
            student = student,
            acceptance = False
        )
        borrowed_book.save()
        serializer = BorrowBookSerializers(borrowed_book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetBorrowedBooks(APIView):
    permission_classes = [IsAuthenticated, LibrarianPermission]
    def get_librarian(self, user):
        try:
            return LibrarianProfile.objects.get(user=user)
        except:
            raise Http404
    
    def get(self, request):
        librarian = self.get_librarian(request.user)
        books = Book.objects.filter(librarian=librarian)
        borrowed_books = BorrowBook.objects.filter(book__in=books)
        serializer = BorrowBookSerializers(borrowed_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)