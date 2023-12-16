from django.shortcuts import redirect, render

from book.models import Book, ProductReview
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
        
        product = Book.objects.get(id=product_id)
        
        ProductReview.objects.create(
            user=user,
            product=product,
            review_text=review_text,
            review_rating=review_rating
        )
        
        return JsonResponse({'status': 'success'})
    return redirect('name_of_your_book_list_view')

# --------------------------

@login_required(login_url="user:login")
def delete_review_book(request, book_id):
    if request.method == 'POST':
        try:
            reader_instance = Reader.objects.get(user=request.user)
            # Ambil objek wishlist yang berhubungan dengan user yang sedang login
            review = ProductReview.objects.get(user=reader_instance)
            
            # Cari buku yang ingin dihapus berdasarkan book_id
            book_to_remove = Book.objects.get(pk=book_id)
            
            # Hapus buku dari wishlist
            review.product.remove(book_to_remove)            
            return JsonResponse({'status': 'ok'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Object not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)



def edit_review(request):
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
    return render(request, 'review_list.html', {'reviews': reviews})

