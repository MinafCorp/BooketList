from django.urls import path, include
from user.views import show_landing, login_user, signup_author, signup_reader, signup, logout_user


app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('signup/', signup, name='signup'),
    path('signup_author/', signup_author, name='signup_author'),
    path('signup_reader/', signup_reader, name='signup_reader'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/books/list_buku/',include('book.urls'), name='daftar_buku'),
    path('wishlist/',include('wishlist.urls'), name='wishlistku'),
] 