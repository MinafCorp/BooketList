from django.contrib import admin
from django.urls import path, include
from book.views import *

app_name = 'book'

urlpatterns = [
    path('', get_book, name='get_book'),
    path('list_buku', list_buku, name='list_buku'),
    path('manajemen-buku/', include('manajemen_buku.urls')),
    path('create_review/', create_review, name='create_review'),
    path('review_list/', review_list, name='review_list'),
]

