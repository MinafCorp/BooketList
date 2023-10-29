from django import forms

class WishlistSearchForm(forms.Form):
    query = forms.CharField(label='Search for a book', max_length=100)