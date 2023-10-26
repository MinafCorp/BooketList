from django.urls import path
from user.views import show_landing

app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
]