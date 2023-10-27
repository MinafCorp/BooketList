from django.db import models
from django.contrib.auth.models import User

class Books (models.Model):
    judul = models.CharField(max_length=255)
    halaman = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images/')
# Create your models here.
