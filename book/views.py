from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from django.core import serializers

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
