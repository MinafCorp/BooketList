from django.db import models
from user.models import Author

# Create your models here.

class Updates(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    data_added = models.DateField(auto_now_add=True)