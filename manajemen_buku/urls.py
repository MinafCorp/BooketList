from django.urls import path
from manajemen_buku.views import *

app_name = 'manajemen_buku'

urlpatterns = [
    path('', manajemen_buku, name='manajemen_buku'),
    path('create-item-ajax/', add_books_ajax, name='add_books_ajax'),
    path('delete-item-ajax/<int:item_id>/', delete_books_ajax, name='delete_books_ajax'),
    path('get-books-ajax/', get_books_json, name='get_books_json'),
    path('delete-books-ajax/<int:item_id>/', delete_books_ajax, name='delete_books_ajax'),
    path('delete_author_book/<int:book_id>/', delete_author_book, name='delete_author_book'),
    path('create-books-ajax/', add_books_ajax, name='add_books_ajax'),
    path('hide-books-ajax/<int:item_id>/', hide_books_ajax, name='hide_books_ajax'),
    path('get-books/', get_books, name='get_books'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json/', show_json, name='show_json'),
    path('delete_book/isbn/<int:isbn>/', delete_book_by_isbn, name='delete_book_by_isbn'),
    path('get_books_json/',get_books_json,name='json'),
]