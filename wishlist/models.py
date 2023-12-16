from django.db import models
from user.models import Reader
from book.models import Book

class Wishlist(models.Model):
    pengguna = models.OneToOneField(Reader, on_delete=models.CASCADE, related_name='wishlist')
    buku = models.ManyToManyField(Book, related_name='wishlists')
