from django.urls import path 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegistrationView,
    StudentView,
    StudentDetailsView,
    LibrarianView,
    LibrarianDetailsView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/user/', RegistrationView.as_view(), name='register_user'),
    path('register/student/', StudentView.as_view(), name='register_student'),
    path('student/<int:pk>/', StudentDetailsView.as_view(), name='edit_student_details'),
    path('register/librarian/', LibrarianView.as_view(), name='register_librarian'),
    path('librarian/<int:pk>/', LibrarianDetailsView.as_view(), name='edit_librarian_details')
]
