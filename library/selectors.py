from django.shortcuts import get_object_or_404
from .models import Book, Author, Genre, BookRequest

def get_latest_books(limit=3):
    return Book.objects.select_related('author', 'genre').order_by('-created_at')[:limit]

def get_filtered_books(query=None, genre_id=None):
    books = Book.objects.select_related('author', 'genre').all()
    if query:
        books = books.filter(title__icontains=query)
    if genre_id:
        books = books.filter(genre_id=genre_id)
    return books

def get_book_detail(pk):
    return get_object_or_404(Book.objects.select_related('author', 'genre'), pk=pk)

def get_all_genres():
    return Genre.objects.all()

def get_all_authors():
    return Author.objects.all()

def get_author_detail(pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.select_related('genre').all()
    return author, books

def get_all_requests():
    return BookRequest.objects.select_related('book', 'book__author').all()