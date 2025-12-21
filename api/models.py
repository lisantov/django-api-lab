from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя автора")
    biography = models.TextField(verbose_name="Биография автора")
    def str(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def str(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор книги")
    year = models.IntegerField(verbose_name="Год выпуска")
    category = models.CharField(max_length=100, verbose_name="Категория книги")
    genre = models.CharField(max_length=100, verbose_name="Жанр книги")
    publisher = models.CharField(max_length=100, verbose_name="Издатель книги")
    cover = models.ImageField(upload_to='covers', null=True, blank=True, verbose_name="Обложка книги")
    text = models.FileField(upload_to='books', verbose_name="Файл с книгой", blank=True, null=True)
    
    def str(self):
        return self.title

    constraints = [
        models.UniqueConstraint(fields=['title', 'author', 'year', 'publisher'], name='unique_book'),
    ]