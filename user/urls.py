from django.urls import path, include
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
] 