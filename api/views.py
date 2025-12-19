from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsStaffOrReadOnly

from api.models import Book
from api.serializers import BookSerializer

class BookList(APIView):
    permission_classes = [IsStaffOrReadOnly]
    def get(iself, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)