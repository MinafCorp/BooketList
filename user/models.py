from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    