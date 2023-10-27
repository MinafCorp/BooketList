from django.contrib import admin
from django.urls import path, include
from book.views import *

urlpatterns = [
    path('', get_book, name='get_book'),
]
