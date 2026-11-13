from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.book_list_view, name='book_list'),
    path('books/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('books/add/', views.book_create_view, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update_view, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete_view, name='book_delete'),
    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', views.author_detail_view, name='author_detail'),
    path('books/<int:pk>/request/', views.request_create_view, name='request_create'),
    path('requests/', views.request_list_view, name='request_list'),
]