from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Donation, Category


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


class AddDonationForm(forms.Form):
    quantity = forms.IntegerField()
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={}),
                                        empty_label=None)
    # institution = forms.ForeignKey('Institution', on_delete=models.CASCADE)
    address = forms.CharField(max_length=128)
    phone_number = forms.IntegerField()
    city = forms.CharField(max_length=128)
    zip_code = forms.CharField(max_length=6)
    pick_up_date = forms.DateField()
    pick_up_time = forms.TimeField()
    pick_up_comment = forms.CharField(widget=forms.TextInput)
