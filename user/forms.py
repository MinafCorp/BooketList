from django.forms import ModelForm
from django import forms
from user.models import User

class UserForm(forms.Form):
    ROLES = (
        ('author', 'author'),
        ('reader', 'reader'),
    )
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    role = forms.ChoiceField(required=True, choices=ROLES, widget=forms.Select(attrs={'class': 'custom-select-class'}))
    class Meta:
        model = User