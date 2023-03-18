from django.db import models
from datetime import timedelta
from users.models import LibrarianProfile, StudentProfile
from library.models import Library

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(default=1)
    available_quantity = models.IntegerField()
    author = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.SET_NULL, null=True)
    librarian = models.ForeignKey(LibrarianProfile, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.name
    
class BorrowBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, null=True)
    acceptance = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now=True)
    returnDate = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.returnDate:
            self.returnDate = self.createdAt.date() + timedelta(days=14)
        super().save(*args, **kwargs)