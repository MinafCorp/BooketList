from django.db import models

from django.contrib.auth.models import User
from user.models import Author

class Publish(models.Model):
    ISBN = models.IntegerField(unique=True, null=True, blank=True)
    title = models.TextField(verbose_name="Book-Title", null=True, blank=True)
    author = models.TextField(null= True, blank=True)
    year_of_publication = models.IntegerField(verbose_name="Year-Of-Publication", null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    authorUser = models.ForeignKey(Author, on_delete=models.CASCADE, null= True, blank=True)
    image = models.ImageField(upload_to='book_images/',null = True, blank = True)

