from django.urls import path
from . import views
from django.contrib import admin
from .views import (
    ListBook,
    BookCreateView,
    BookUpdateView,
    listbooks,
    BookDeleteView,
    book_list
)

app_name = "main"
#This are all URL Patterns which will be used for Books
urlpatterns = [
    path('', ListBook.as_view(), name='home'),
    path('book/<book_id>', views.listbooks, name='book'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/new/', BookCreateView, name='book-create'),
    path('book-update/<book_id>/', BookUpdateView.as_view(), name='book-update'),
    path('book-delete/<book_id>/', BookDeleteView.as_view(), name='book-delete'),
]
