from rest_framework import serializers
from .models import Author, Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'category', 'genre', 'publisher', 'cover', 'text']

    def validate_year(self, value):
        if value < 1000 or value > 9999:
            raise serializers.ValidationError('Year must be between 1000 and 9999')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']

    def get_books(self, obj):
        if obj.id:
            return (book.id for book in Book.objects.filter(author=obj.id))
        return []

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']