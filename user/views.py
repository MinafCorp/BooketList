from django.shortcuts import render
from user.forms import UserCreationForm
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from .models import User, Author, Reader

# Create your views here.
def show_landing(request):
    return render(request, 'landing.html')

def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            selected_role = request.POST.get('role')
            if selected_role == 'author':
                author = Author(user=user)
                author.save()
                user.is_author = True
                user.save()
            elif selected_role == 'reader':
                reader = Reader(user=user)
                reader.save()
                user.is_reader = True
                user.save()
            return redirect('user:login')
    context = {'form':form}
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        user = authenticate(request, username=username, password=password, role=role)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)