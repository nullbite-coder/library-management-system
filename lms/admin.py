from django.contrib import admin
from .models import Book
from django.db import models

#Varibales to use in admin dashboard, to add a book or delete
class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book ID", {'fields': ["book_id"]}),
        ("Book Title", {'fields': ["book_title"]}),
        ("Author", {'fields': ["author"]}),
        ("Language", {'fields': ["language"]}),
        ("No. of Pages", {'fields': ["pages"]}),
        ("Price", {'fields': ["price"]}),
        ("Overview", {'fields': ["overview"]})

    ]
    list_display = ('book_id','book_title','author','language','pages','price','overview')


admin.site.register(Book,ItemAdmin)
