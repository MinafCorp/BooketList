from django import forms
from django.forms import ModelForm
from book.models import Book
from book.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['user', 'product', 'review_text', 'review_rating']