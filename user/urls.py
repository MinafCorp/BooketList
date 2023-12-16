from django.urls import path, include
from manajemen_buku.views import get_books
from user.views import *

app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('home/', show_home, name='show_home'),
    path('signup/', signup, name='signup'),
    path('signup_author/', signup_author, name='signup_author'),
    path('signup_reader/', signup_reader, name='signup_reader'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-user/', delete_user, name='delete_user'),
    
    path('get-books/', get_books, name='get_books'),
    path('api/books/list_buku/',include('book.urls'), name='daftar_buku'),
    path('list_buku/',include('book.urls'), name='daftar_buku'),
    
    path('wishlist/',include('wishlist.urls'), name='wishlistku'),
    path('profile/', profile, name='profile'),
    path('user-api/', user_info, name='user_info'),
] 