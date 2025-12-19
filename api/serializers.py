from rest_framework import serializers
from .models import Author, Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'category', 'genre', 'publisher', 'cover', 'text']

        def validate_year(self, year):
            if year < 1000 or year > 9999:
                raise serializers.ValidationError('Year must be between 1000 and 9999')
            return year


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']