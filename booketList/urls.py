from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api/books/',include('book.urls')),
    path('manajemen-buku/', include('manajemen_buku.urls')),
    path('updates/', include('updates.urls')),
]
#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
