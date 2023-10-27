from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from django.core import serializers

def get_book(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")
# Create your views here.
