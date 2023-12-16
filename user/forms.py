from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User
from django.db import transaction
from .models import Reader, Author

class ReaderSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self):
        user = super().save(commit=False)
        user.role = 'READER'
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        reader = Reader.objects.create(user=user)
        reader.save()
        return user
    
class AuthorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.role = 'AUTHOR'
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        author = Author.objects.create(user = user)
        author.save()
        return user 
    

class ProductSearchForm(forms.Form):
    title_query = forms.CharField(label='Search by Title', max_length=100, required=False)
    