from django.shortcuts import render, redirect
from django.contrib import messages
from .selectors import (
    get_latest_books, get_filtered_books, get_book_detail,
    get_all_genres, get_all_authors, get_author_detail, get_all_requests
)
from .services import create_book_request
from .forms import BookForm, BookRequestForm
from .decorators import staff_required


def home_view(request):
    latest_books = get_latest_books(3)
    return render(request, 'library/home.html', {'latest_books': latest_books})


def book_list_view(request):
    query = request.GET.get('q', '')
    genre_id = request.GET.get('genre', '')

    books = get_filtered_books(query=query, genre_id=genre_id if genre_id else None)
    genres = get_all_genres()

    context = {
        'books': books,
        'genres': genres,
        'selected_genre': int(genre_id) if genre_id else None,
        'search_query': query,
    }
    return render(request, 'library/book_list.html', context)


def book_detail_view(request, pk):
    book = get_book_detail(pk)
    return render(request, 'library/book_detail.html', {'book': book})


@staff_required
def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Книгу успішно створено!")
            return redirect('library:book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Створити'})


@staff_required
def book_update_view(request, pk):
    book = get_book_detail(pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Книгу успішно оновлено!")
            return redirect('library:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Редагувати'})


@staff_required
def book_delete_view(request, pk):
    book = get_book_detail(pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Книгу успішно видалено!")
        return redirect('library:book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})


def author_list_view(request):
    authors = get_all_authors()
    return render(request, 'library/author_list.html', {'authors': authors})


def author_detail_view(request, pk):
    author, books = get_author_detail(pk)
    return render(request, 'library/author_detail.html', {'author': author, 'books': books})


def request_create_view(request, pk):
    book = get_book_detail(pk)
    if not book.is_available:
        messages.error(request, "Цю книгу видано, бронювання неможливе.")
        return redirect('library:book_detail', pk=book.pk)

    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            create_book_request(book, form.cleaned_data)
            messages.success(request, "Заявку на бронювання успішно прийнято!")
            return redirect('library:book_detail', pk=book.pk)
    else:
        form = BookRequestForm()
    return render(request, 'library/request_form.html', {'form': form, 'book': book})


@staff_required
def request_list_view(request):
    requests = get_all_requests()
    return render(request, 'library/request_list.html', {'requests': requests})