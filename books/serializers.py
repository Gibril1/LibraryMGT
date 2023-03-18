from rest_framework import serializers
from .models import Book, BorrowBook

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowBook
        fields = '__all__'