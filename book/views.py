from django.shortcuts import render
from book.models import Book, ProductReview
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
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
    
    form = ProductReview()
    context = {
        'products': data,
        'wishlisted_book_ids': wishlisted_book_ids,
        'form':form
    }
    return render(request,'list_buku.html', context)


def review(request):
    title_search = request.GET.get('bookTitleSearch', '')
    year_filter = request.GET.get('yearFilter', 'all')
    reader = request.user.reader

    # Dapatkan buku yang ada di wishlist user yang sedang login
    user_wishlist_books = Wishlist.objects.filter(pengguna=reader).values_list('buku', flat=True)
    books = Book.objects.filter(pk__in=user_wishlist_books, title__icontains=title_search)

    if year_filter == '<1990':
        books = books.filter(year_of_publication__lt=1990)
    elif year_filter == '1990-2000':
        books = books.filter(year_of_publication__gte=1990, year_of_publication__lte=2000)
    elif year_filter == '>2000':
        books = books.filter(year_of_publication__gt=2000)

    books_data = [
        {
            'pk': book.pk,
            'title': book.title,
            'image_url_l': book.image_url_l,
            'author': book.author,
            'year': book.year_of_publication,
        }
        for book in books
    ]
    return JsonResponse({'books': books_data})



