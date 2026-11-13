from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ПІБ автора")
    country = models.CharField(max_length=80, verbose_name="Країна")
    birth_year = models.IntegerField(null=True, blank=True, verbose_name="Рік народження")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name="Назва книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="Автор")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="books", verbose_name="Жанр")
    year = models.IntegerField(verbose_name="Рік видання")
    pages = models.IntegerField(verbose_name="Кількість сторінок")
    description = models.TextField(blank=True, verbose_name="Опис")
    is_available = models.BooleanField(default=True, verbose_name="Доступна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="requests", verbose_name="Книга")
    reader_name = models.CharField(max_length=100, verbose_name="Ім'я читача")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    class Meta:
        verbose_name = "Заявка на бронювання"
        verbose_name_plural = "Заявки на бронювання"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка від {self.reader_name} на '{self.book.title}'"