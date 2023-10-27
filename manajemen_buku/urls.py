from django.urls import path, include
from manajemen_buku.views import add_books_ajax, delete_books_ajax, get_books_json, manajemen_buku
from manajemen_buku.views import manajemen_buku,  show_json,show_json_by_id 
from manajemen_buku.views import increment_amount, decrement_amount, delete_books
from manajemen_buku.views import get_books_json, add_books_ajax


app_name = 'manajemen_buku'

urlpatterns = [
    path('', manajemen_buku, name='manajemen_buku'),
    path('create-item-ajax/', add_books_ajax, name='add_books_ajax'),
    path('delete-item-ajax/<int:item_id>/', delete_books_ajax, name='delete_books_ajax'),
    path('get-books/', get_books_json, name='get_books_json'),
    path('delete-books-ajax/<int:item_id>/', delete_books_ajax, name='delete_books_ajax'),
    path('create-books-ajax/', add_books_ajax, name='add_books_ajax'),

    
]