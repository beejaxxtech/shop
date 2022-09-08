
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import *


class ProductSearchForm(forms.ModelForm):
    name_of_product = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control mr-sm-2", 'placeholder': 'Enter name of product'}))

    class Meta:
        model = ProductSearch
        fields = ['name_of_product',]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
