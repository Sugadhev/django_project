from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import RegisterForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class MyRegisterForm(forms.ModelForm):
    class Meta:
        model= RegisterForm
        fields=["location", "medicinename", "medicinecategory", "symptoms",]