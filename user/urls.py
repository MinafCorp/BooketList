from django.urls import path
from user.views import show_landing, signup, login, signup_author, signup_reader

app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('signup/', signup, name='signup'),
    path('signup_author/', signup_author, name='signup_author'),
    path('signup_reader/', signup_reader, name='signup_reader'),
    path('login/', login, name='login'),
]