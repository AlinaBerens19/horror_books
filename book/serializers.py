from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'published_date', 'publisher', 'language', 'genre', 'ranking', 'highlighted', 'updated', 'image', 'category', 'owner', 'trending')
