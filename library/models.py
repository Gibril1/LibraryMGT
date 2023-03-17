from django.db import models
from django.utils import timezone
from users.models import LibrarianProfile

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    librarian= models.ForeignKey(LibrarianProfile, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name