import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect
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
from manajemen_buku.models import Book


# Create your views here.
@login_required(login_url='/manajemen_buku/login')
def manajemen_buku(request):
    context = {
        'nama': request.user.username, # Nama kamu
        'products': Book.objects.filter(user=request.user)
    }

    return render(request, "manajemen_buku.html", context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('manajemen_buku:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("manajemen_buku:manajemen_buku")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increment_amount(request, item_id):
    books = Book.objects.get(pk=item_id)
    books.halaman += 1
    books.save()
    return redirect('main:show_main')

def decrement_amount(request, item_id):
    books = Book.objects.get(pk=item_id)
    if books.halaman > 0:
        books.halaman -= 1
        books.save()
    if books.halaman == 0:
        books.delete()
    return redirect('main:show_main')

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
        judul = request.POST.get("judul")
        halaman = request.POST.get("halaman")
        description = request.POST.get("description")
        user = request.user
        image = request.FILES.get('image')


        new_item = Book(judul=judul, halaman=halaman, description=description, user=user, image=image)
        new_item.save()

        return HttpResponse("CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_books_ajax(request, item_id):
    if request.method == 'DELETE':
        books = Book.objects.get(id=item_id)
        books.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)
