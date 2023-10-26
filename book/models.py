from django.db import models

# Create your models here.
class Book(models.Model):
    ISBN = models.IntegerField(unique=True, null=True, blank=True)
    title = models.TextField(verbose_name="Book-Title", null=True, blank=True)
    author = models.TextField(verbose_name="Book-Author", null=True, blank=True)
    year_of_publication = models.IntegerField(verbose_name="Year-Of-Publication", null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_url_s = models.URLField(verbose_name="Image-URL-S", null=True, blank=True)
    image_url_m = models.URLField(verbose_name="Image-URL-M", null=True, blank=True)
    image_url_l = models.URLField(verbose_name="Image-URL-L", null=True, blank=True)
    