from django.shortcuts import render
from user.forms import ReaderSignUpForm, AuthorSignUpForm
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from .models import User, Author, Reader

# Create your views here.
def show_landing(request):
    return render(request, 'landing.html')

def reader_register(request):
    form = ReaderSignUpForm()
    
    if request.method == 'POST':
        form = ReaderSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context =  {'form': form}
    return render(request, 'signup_reader.html', context)

def author_register(request):
    form = AuthorSignUpForm()
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context =  {'form': form}
    return render(request, 'signup_author.html', context)
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if user.is_author:
                    return(redirect("manajamen_buku: manajemen_buku."))
                else:
                    return(redirect("something"))
        
    return render(request, 'login.html', context={'form': AuthenticationForm()})

def logout(request):
    logout(request)
    return redirect('login')