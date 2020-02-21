from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Donation


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label=False)  # to jest pole email
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label=False)


class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['user']
