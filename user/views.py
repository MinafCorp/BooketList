import datetime
from django.shortcuts import render
from book.models import Book
from user.forms import ReaderSignUpForm, AuthorSignUpForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from book.models import Book
from user.models import Reader
from wishlist.models import Wishlist

@login_required(login_url='user:login')
def show_home(request):
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
    return render(request,'home.html', context)

def show_landing(request):
    return render(request, 'landing.html')

def signup(request):
    return render(request, 'signup.html')

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
            role = form.cleaned_data.get('role')
            user = authenticate(username=username, password=password, role= role)
            if user is not None:
                login(request,user)
                if user.role == 'AUTHOR':
                    response = HttpResponseRedirect(reverse('manajemen_buku:manajemen_buku'))
                elif user.role == 'READER':
                    response = HttpResponseRedirect(reverse('user:show_home'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
    return render(request, 'login.html', context={'form': AuthenticationForm()})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('user:show_landing'))
    response.delete_cookie('last_login')
    return response
