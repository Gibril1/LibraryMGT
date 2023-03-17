from django.urls import path

from .views import (
    BookCreateView,
    BookDetailsView,
    BookView
)

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='create_book'),
    path('<int:pk>/', BookDetailsView.as_view(), name='book_details'),
    path('', BookView.as_view(), name='get_books')
]