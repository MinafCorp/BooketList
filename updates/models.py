from django.db import models
from user.models import User

# Create your models here.

class Updates(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    data_added = models.DateField(auto_now_add=True)

    def username(self):
        return self.author.username()