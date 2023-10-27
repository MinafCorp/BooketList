from django.urls import path
from user.views import show_landing, reader_register, author_register, login, logout

app_name = 'user'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('reader_register/', reader_register, name='reader_register'),
    path('author_register/', author_register, name='author_register'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
]