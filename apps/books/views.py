from django.shortcuts import render
from django.http import JsonResponse

# import rest_framework dependencies 
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.books.models import Books
from .serializers import BookSerializer

class BooksList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookSubmit(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    