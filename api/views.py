from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsStaffOrReadOnly

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer

permissions.IsAdminUser
class BookList(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorList(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)