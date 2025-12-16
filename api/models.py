from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def str(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def str(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок книги")
    authors = models.ManyToManyField(Author, verbose_name="Автор книги")
    year = models.IntegerField(max_length=4, verbose_name="Год выпуска")
    category = models.CharField(max_length=100, verbose_name="Категория книги")
    genre = models.CharField(max_length=100, verbose_name="Жанр книги")
    publisher = models.CharField(max_length=100, verbose_name="Издатель книги")
    cover = models.ImageField(upload_to='covers', null=True, blank=True, verbose_name="Обложка книги")
    text = models.FileField(upload_to='books', verbose_name="Файл с книгой")
    def str(self):
        return self.title
    # уникальность
    constraints = [
        models.UniqueConstraint(fields=['title', 'author', 'year', 'publisher'], name='unique_book'),
    ]