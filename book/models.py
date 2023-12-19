from django.db import models
from user.models import *

# Create your models here.
class Book(models.Model):
    ISBN = models.IntegerField(unique=True, null=True, blank=True)
    title = models.TextField(verbose_name="Book-Title", null=True, blank=True)
    author = models.TextField(null= True, blank=True)
    year_of_publication = models.IntegerField(verbose_name="Year-Of-Publication", null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_url_s = models.URLField(verbose_name="Image-URL-S", null=True, blank=True)
    image_url_m = models.URLField(verbose_name="Image-URL-M", null=True, blank=True)
    image_url_l = models.URLField(verbose_name="Image-URL-L", null=True, blank=True)
    authorUser = models.ForeignKey(Author, on_delete=models.CASCADE, null= True, blank=True)
    image = models.ImageField(upload_to='book_images/',null = True, blank = True)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review_rating = models.IntegerField()
    created_by = models.TextField(null=True)
    judul_buku = models.TextField(null=True)

    def edit_data(self, review_text, review_rating):
        self.review_text = review_text
        self.review_rating = review_rating
        self.save()

    