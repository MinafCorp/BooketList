import datetime
from django.shortcuts import render
from user.forms import ReaderSignUpForm, AuthorSignUpForm
import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from book.models import Book
from .models import Reader, User
from wishlist.models import Wishlist

from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='user:login')
def show_home(request):
    data = Book.objects.all()
    
    if request.user.is_authenticated:
        reader_instance, _ = Reader.objects.get_or_create(user=request.user)
        wishlist_instance, _ = Wishlist.objects.get_or_create(pengguna=reader_instance)
        wishlisted_books = wishlist_instance.buku.all()
        wishlisted_book_ids = set(book.id for book in wishlisted_books)
    else:
        wishlisted_book_ids = set()  # Jika pengguna belum masuk, set kosong
    
    context = {
        'products': data,
        'wishlisted_book_ids': wishlisted_book_ids,
    }
    return render(request,'home.html', context)

def show_landing(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html')

def signup_reader(request):
    form = ReaderSignUpForm()
    
    if request.method == 'POST':
        form = ReaderSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return HttpResponseRedirect(reverse('user:login'))
    context =  {'form': form}
    return render(request, 'signup_reader.html', context)

def signup_author(request):
    form = AuthorSignUpForm()
    
    if request.method == 'POST':
        form = AuthorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return HttpResponseRedirect(reverse('user:login'))
        
    context =  {'form': form}
    return render(request, 'signup_author.html', context)
    

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = request.POST.get('role')
            user = authenticate(username=username, password=password)
            if user is not None and user.role == role:
                login(request, user)
                if user.role == 'AUTHOR':
                    response = HttpResponseRedirect(reverse('manajemen_buku:manajemen_buku'))
                elif user.role == 'READER':
                    response = HttpResponseRedirect(reverse('user:show_home'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Username/password salah atau role tidak sesuai')
    return render(request, 'login.html', context={'form': AuthenticationForm()})


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('user:show_landing'))
    response.delete_cookie('last_login')
    return response

#def get_books(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def delete_user(request):
    user = request.user
    user.delete()
    return HttpResponseRedirect(reverse('user:show_landing'))

@csrf_exempt
def user_info(request):
    # Assuming the request user is the target user
    data = request.user
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")
