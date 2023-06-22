from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from . import permissions


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    permission_classes = (permissions.IsOwnerOrReadOnly,)

