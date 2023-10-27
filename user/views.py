from django.shortcuts import render
from user.forms import ReaderSignUpForm, AuthorSignUpForm
import datetime
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
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
            role = form.cleaned_data.get('role')
            user = authenticate(username=username, password=password, role= role)
            if user is not None:
                login(request,user)
                if user.role == 'AUTHOR':
                    response = HttpResponseRedirect(reverse('manajemen_buku:manajemen_buku'))
                elif user.role == 'READER':
<<<<<<< HEAD
                    response = HttpResponseRedirect(reverse('main:show_main'))
=======
                    response = render(request, 'home.html')
            response.set_cookie('last_login', str(datetime.datetime.now()))
>>>>>>> 51f3217110f9eb46dde57db6ebaa64f4d5b9b080
            return response
        
    return render(request, 'login.html', context={'form': AuthenticationForm()})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('user:show_landing'))
<<<<<<< HEAD
=======
    response.delete_cookie('last_login')
>>>>>>> 51f3217110f9eb46dde57db6ebaa64f4d5b9b080
    return response