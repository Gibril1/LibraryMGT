from .serializers import RegistrationSerializer, StudentSerializer, LibrarianSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentProfile, LibrarianProfile, User
from app.permissions import StudentPermission, LibrarianPermission, UserEditDeletePermission


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class StudentView(APIView):
    permission_classes =[IsAuthenticated, StudentPermission]
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class StudentDetailsView(RetrieveUpdateAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
    

class LibrarianView(CreateAPIView):
    permission_classes = [IsAuthenticated, LibrarianPermission]
    def post(self, request):
        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class LibrarianDetailsView(RetrieveUpdateAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission, IsAuthenticated]
    queryset = LibrarianProfile.objects.all()
    serializer_class = LibrarianSerializer

