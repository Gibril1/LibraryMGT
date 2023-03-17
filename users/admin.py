from django.contrib import admin
from .models import User, StudentProfile,LibrarianProfile

# Register your models here.
admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(LibrarianProfile)
