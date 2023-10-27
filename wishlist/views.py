from django.shortcuts import redirect
from .models import Wishlist
from book.models import Book
from user.models import Reader

def add_book_to_wishlist(request, book_id):
    user = request.user
    # Pastikan user sudah login dan adalah seorang Reader
    if user.is_authenticated and isinstance(user, Reader):
        wishlist, created = Wishlist.objects.get_or_create(pengguna=user)
        book = Book.objects.get(id=book_id)
        wishlist.buku.add(book)
        # Redirect ke halaman yang diinginkan setelah menambahkan buku
        return redirect('some_view_name')
    else:
        # Handle untuk user yang tidak login atau bukan seorang Reader
        return redirect('login_view_name')