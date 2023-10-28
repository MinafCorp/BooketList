from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from book.forms import ProductForm
from book.models import Book  # Assuming your Product model is defined in 'main.models'
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def get_book(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def list_buku(request):
    data = Book.objects.all()
    context = {
        'products' : data,
    }
    return render(request,'list_buku.html', context)
# Create your views here.



