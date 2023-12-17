import datetime
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from book.models import Book
from manajemen_buku.models import Publish
from user.models import Author, Reader


# Create your views here.
@login_required(login_url='/login')
def manajemen_buku(request):
    author_instance = Author.objects.get(user=request.user)
    context = {
        'username': request.user.username,
        'products': Book.objects.filter(authorUser=author_instance), # Tambahkan ini
    }

    return render(request, "manajemen_buku.html", context)


def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def delete_books(request, item_id):
    books = Book.objects.get(pk=item_id)
    books.delete()
    return redirect('main:show_main')

def get_books_json(request):
    author_instance = Author.objects.get(user=request.user)
    product_item = Book.objects.filter(authorUser=author_instance)
    return HttpResponse(serializers.serialize('json', product_item))

def get_books(request):
    author_instance = Author.objects.get(user=request.user)
    product_item = Publish.objects.filter(authorUser=author_instance)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_books_ajax(request):
    if request.method == 'POST':
        ISBN = request.POST.get("ISBN")
        title = request.POST.get("title")
        author = request.POST.get("author")
        year_of_publication = request.POST.get('year_of_publication')
        publisher = request.POST.get("publisher")
        image_url_s = request.FILES.get("image")
        image_url_m = ""
        image_url_l = ""
        authorUser = Author.objects.get(user=request.user)
        image = request.FILES.get("image")


        new_item = Book(ISBN=ISBN, title=title, author=author, year_of_publication=year_of_publication, publisher=publisher, image_url_s=image_url_s, image_url_m=image_url_m, image_url_l=image_url_l, authorUser=authorUser, image=image)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_books_ajax(request, item_id):
    if request.method == 'DELETE':
        books = Book.objects.get(id=item_id)
        books.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)

@csrf_exempt
def delete_author_book(request, book_id):
    if request.method == 'POST':
        try:
            books = Book.objects.get(id=book_id)
            books.delete()
            
            return JsonResponse({"success": True, "message": "Berhasil dihapus dari your books"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Object not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def hide_books_ajax(request, item_id):
    if request.method == 'DELETE':
        books = Publish.objects.get(id=item_id)
        books.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        user_id = request.user.id
        print(f"User ID: {user_id}")
        #print(data)
        #print(type(data["ISBN"]))

        new_product = Book.objects.create(
            ISBN = int(data["ISBN"]),
            title = data["title"],
            author=user_id,
            year_of_publication = int(data["YearOfPublication"]),
            publisher = data["publisher"],
            image_url_s = "",
            image_url_m = "",
            image_url_l = "",
            image = "",
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_book_by_isbn(request, isbn):
    print(isbn)
    try:
        book = Book.objects.get(ISBN=isbn)
        book.delete()
        return JsonResponse({'status': 'success', 'message': 'Book deleted successfully'})
    except Book.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)