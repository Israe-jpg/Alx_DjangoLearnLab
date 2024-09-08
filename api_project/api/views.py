from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
# generics.ListAPIView
