from django.shortcuts import redirect, render

from book.models import Book, ProductReview
from user.models import User, Reader
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
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

@login_required
def create_review(request):
    if request.method == "POST":
        user = request.user
        product_id = request.POST.get('product_id')
        review_text = request.POST.get('review_text')
        review_rating = request.POST.get('review_rating')
        nama_user = str(user)
               
        product = Book.objects.get(id=product_id)
        judul = str(product.title)
        
        ProductReview.objects.create(user = user, product=product, review_text=review_text, review_rating=review_rating, created_by = nama_user,
                                     judul_buku = judul
        )
        return JsonResponse({'status': 'success'})
    review_list()

@login_required
def show_review(request):
    reader_instance = Reader.objects.get(user=request.user)
    review_instance = ProductReview.objects.get(pengguna=reader_instance)
    reviewed_books = review_instance.product.all()
    context = {
        'review': reviewed_books,
        'user_data': reader_instance,
    }
    return render(request, 'review_list.html', context)

def review_api(request):
    if request.user.is_authenticated:
        try:
            reader_instance = Reader.objects.get(user=request.user)
            review_instance = ProductReview.objects.get(pengguna=reader_instance)
            reviewed_books = review_instance.product.all()

            books_data = [
                {
                    'pk': book.pk,
                    'title': book.title,
                    'image_url_l': book.image_url_l,
                    'author': book.author,
                    'year': book.year_of_publication,
                    'review_text': reviewed_books.review_text,
                    'review_rating': reviewed_books.review_rating,
                }
                for book in reviewed_books
            ]

            return JsonResponse({'books': books_data})
        except ProductReview.DoesNotExist:
            return JsonResponse({'books': []})  # Return an empty list if the review doesn't exist
    return JsonResponse({'books': []})  # Return an empty list if the user is not authenticated


@login_required(login_url="user:login")
def delete_review_book(request, book_id):
            product = ProductReview.objects.get(pk=book_id)
            product.delete()
            return JsonResponse({'status': 'ok'})



def review_list_yours(request):
    reviews = ProductReview.objects.all()
    reader_instance = Reader.objects.get(user=request.user)
    wishlist_instance = ProductReview.objects.filter(user=request.user)
    # wishlisted_books = wishlist_instance.product.all()
    user_sekarang = request.user
    context = {
        'reviews': wishlist_instance,
        "user_sekarang":user_sekarang,
        'how': wishlist_instance,
    }
    # response = JsonResponse(context, status=200)
    return render(request, 'review_list_yours.html', context)


def edit_review(request):
    print("hehe")
    if request.method == "POST":
        user = request.user
        product_id = request.POST.get('product_id')
        review_text = request.POST.get('review_text')
        review_rating = request.POST.get('review_rating')
        product = Book.objects.get(id=product_id)
        ProductReview.filter(pk=product_id).update(user=user,
            product=product,
            review_text=review_text,
            review_rating=review_rating)
        
        
        return JsonResponse({'status': 'success'})
    return redirect('name_of_your_book_list_view')

@login_required
def review_list(request):
    reviews = ProductReview.objects.all()
    reader_instance = Reader.objects.get(user=request.user)
    wishlist_instance = ProductReview.objects.filter(user=request.user)
    # wishlisted_books = wishlist_instance.product.all()
    user_sekarang = request.user
    context = {
        'reviews': reviews,
        "user_sekarang":user_sekarang,
        'how': wishlist_instance,
    }
    # response = JsonResponse(context, status=200)
    return render(request, 'review_list.html', context)

def review_api(request):
    if request.user.is_authenticated:
        try:
            reader_instance = Reader.objects.get(user=request.user)
            review_instance = ProductReview.objects.get(pengguna=reader_instance)
            reviewed_books = review_instance.product.all()

            books_data = [
                {
                    'pk': book.pk,
                    'title': book.title,
                    'image_url_l': book.image_url_l,
                    'author': book.author,
                    'year': book.year_of_publication,
                    'review_text': reviewed_books.review_text,
                    'review_rating': reviewed_books.review_rating,
                }
                for book in reviewed_books
            ]

            return JsonResponse({'books': books_data})
        except ProductReview.DoesNotExist:
            return JsonResponse({'books': []})  # Return an empty list if the review doesn't exist
    return JsonResponse({'books': []})
