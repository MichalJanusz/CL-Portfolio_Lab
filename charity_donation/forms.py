from django import forms
from django.core.exceptions import ValidationError

from .models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Imię'}), label=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}), label=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label=False)
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz Hasło'}), label=False)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        email = cleaned_data.get('email')
        db_email = User.objects.filter(email=email)

        if len(db_email) > 0:
            raise ValidationError('Email zajęty!')

        if password != re_password:
            raise ValidationError('Hasła są niezgodne!')

