from django.db import models
from users.models import LibrarianProfile
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