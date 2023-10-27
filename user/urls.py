from django.urls import path
from user.views import show_landing, signup, login

app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]