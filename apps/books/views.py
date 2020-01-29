from django.shortcuts import render
from django.http import JsonResponse

# import rest_framework dependencies 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.books.models import Books
from .serializers import BookSerializer

class BooksList(APIView):
    def get(self, request, format=None):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    def get(self, request, pk, format=None):
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)


class BookSubmit(APIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)