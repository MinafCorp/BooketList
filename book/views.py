from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

from user.models import Reader
from wishlist.models import Wishlist

def get_book(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def list_buku(request):
    data = Book.objects.all()
    
    # Cek apakah pengguna sudah masuk atau belum
    if request.user.is_authenticated:
        reader_instance = Reader.objects.get(user=request.user)
        # Ambil wishlist pengguna saat ini
        wishlist_instance = Wishlist.objects.get(pengguna=reader_instance)
        wishlisted_books = wishlist_instance.buku.all()
        wishlisted_book_ids = set(book.id for book in wishlisted_books)
    else:
        wishlisted_book_ids = set()  # Jika pengguna belum masuk, set kosong
    
    context = {
        'products': data,
        'wishlisted_book_ids': wishlisted_book_ids,
    }
    return render(request,'list_buku.html', context)



