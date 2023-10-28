from django.urls import path
from updates.views import *

urlpatterns = [
    path('post/', post_update, name='post_update'),
    path('get-updates', get_updates_json, name='get_updates_json')
]