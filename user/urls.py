from django.urls import path, include
from user.views import show_landing, login_user, signup_author, signup_reader, signup, logout_user


app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('signup/', signup, name='signup'),
    path('signup_author/', signup_author, name='signup_author'),
    path('signup_reader/', signup_reader, name='signup_reader'),
    path('login/', login_user, name='login'),
    path('manajemen', include('manajemen_buku.urls')),
    path('logout/', logout_user, name='logout'),
]