from django.forms import ModelForm
from manajemen_buku import Publish

class PublishForm(ModelForm):
    class Meta:
        model = Publish
        fields = ["ISBN", "title", "author", "year_of_publication", "publisher", "authorUser", "image"]