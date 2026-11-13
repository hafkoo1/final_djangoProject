from django.contrib import admin
from .models import Author, Genre, Book, BookRequest

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country', 'birth_year')
    search_fields = ('full_name', 'country')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'year', 'is_available')
    list_filter = ('genre', 'is_available', 'year')
    search_fields = ('title', 'author__full_name')

@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    list_display = ('reader_name', 'book', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('reader_name', 'phone', 'book__title')