from django.urls import path

from .views import (
    LibraryCreateView,
    LibraryView,
    LibraryDetailsView,
    GetLibraryDetailsView
)

urlpatterns = [
    path('', LibraryView.as_view(), name='list_libraries'),
    path('create/', LibraryCreateView.as_view(), name='create_library'),
    path('<int:pk>/', LibraryDetailsView.as_view(), name='edit_details'),
    path('get/<int:pk>/', GetLibraryDetailsView.as_view(), name='get_details')
]