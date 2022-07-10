from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# This will be used to create variables for books and save it in MYSQL database

class Book(models.Model): 
    book_title = models.CharField(max_length=150)
    author = models.CharField(max_length=250,blank=True)
    book_id = models.CharField(max_length=50,blank=True)
    price = models.FloatField()
    pages = models.IntegerField(default=6)
    language = models.CharField(max_length=25, blank=True)
    overview = models.CharField(max_length=500, blank = True)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse("main:book", kwargs={'book_id': self.book_id})

    def get_item_delete_url(self):
        return reverse("main:book-delete", kwargs={'book_id': self.book_id})

    def get_update_item_url(self):
        return reverse("main:book-update", kwargs={'book_id': self.book_id})
