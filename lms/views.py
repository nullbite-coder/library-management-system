from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import admin
from .models import Book
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .decorators import *
from django.db.models import Sum

class ListBook(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'

#This will give return you to the specific page of the book.
def listbooks(request, book_id):
    item = Book.objects.filter(book_id=book_id).first()
    context = {
        'item' : item
    }
    return render(request, 'books.html', context)



#To add a new book in our database
@login_required
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['book_title', 'author', 'book_id', 'price', 'pages', 'language','overview']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

#To update book in our database
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['book_title', 'author', 'book_id', 'price', 'pages', 'language','overview']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return False

#To delete a book in our database
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/book_list'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return False
#this is admin view for to list all the books in our database
@login_required(login_url='/accounts/login/')
@admin_required
def book_list(request):
    items = Book.objects.filter(created_by=request.user)
    context = {
        'items':items
    }
    return render(request, 'book_list.html', context)


