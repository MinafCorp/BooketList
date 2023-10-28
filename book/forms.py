from django.forms import ModelForm
from book.models import Book
from book.models import ProductReview

class ProductForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ('review_text', 'review_rating')