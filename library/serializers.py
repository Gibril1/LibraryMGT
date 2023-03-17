from rest_framework.serializers import ModelSerializer
from .models import Library

class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'