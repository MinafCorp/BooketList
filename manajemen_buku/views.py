from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
# from django.urls import reverse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from book.models import Book
from user.models import Author


# Create your views here.

def manajemen_buku(request):
    context = {
        'products': Book.objects.all()
    }

    return render(request, "manajemen_buku.html", context)




# def increment_amount(request, item_id):
#     books = Book.objects.get(pk=item_id)
#     books.halaman += 1
#     books.save()
#     return redirect('main:show_main')

# def decrement_amount(request, item_id):
#     books = Books.objects.get(pk=item_id)
#     if books.halaman > 0:
#         books.halaman -= 1
#         books.save()
#     if books.halaman == 0:
#         books.delete()
#     return redirect('main:show_main')

def delete_books(request, item_id):
    books = Book.objects.get(pk=item_id)
    books.delete()
    return redirect('main:show_main')

def get_books_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_books_ajax(request):
    if request.method == 'POST':
        ISBN = request.POST.get("ISBN")
        title = request.POST.get("title")
        year_of_publication = request.POST.get("year_of_publication")
        author = request.author
        publisher = request.POST.get("publisher")
        image_url_s = ""
        image_url_m = ""
        image_url_l = ""
        image = request.FILES.get('image')


        new_item = Book(ISBN=ISBN, title=title, year_of_publication=year_of_publication, publisher=publisher, image_url_l=image_url_l, image_url_m=image_url_m, image_url_s=image_url_s, image=image, author=author)
        new_item.save()

        return HttpResponse("CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_books_ajax(request, item_id):
    if request.method == 'DELETE':
        books = Book.objects.get(id=item_id)
        books.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)
