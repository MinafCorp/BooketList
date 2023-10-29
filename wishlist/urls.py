from django.urls import path
from .views import show_wishlist, add_to_wishlist, delete_wishlist_book

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'), 
    path('add_to_wishlist/<int:book_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('delete-wishlist-book/<int:book_id>/', delete_wishlist_book, name='delete-wishlist-book'),

]