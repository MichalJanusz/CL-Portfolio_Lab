from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, RegisterForm, AddDonationForm
from .models import Donation, Institution, Category, User


class LandingPageView(View):
    def get(self, request):
        bags_agregate = Donation.objects.aggregate(Sum('quantity'))
        bags_count = bags_agregate['quantity__sum'] if bags_agregate['quantity__sum'] is not None else 0
        institutions_count = len(Institution.objects.all())
        foundations = Institution.objects.filter(type=1)
        organisations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        ctx = {'bags_count': bags_count, 'institutions_count': institutions_count, 'foundations': foundations,
               'organisations': organisations, 'local_collections': local_collections}
        return render(request, 'charity_donation/index.html', ctx)


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddDonationForm()
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'charity_donation/form.html', {'categories': categories, 'institutions': institutions,
                                                              'form': form})


class LogInView(LoginView):
    template_name = 'charity_donation/login.html'
    authentication_form = LoginForm


class LogOutView(LogoutView):
    pass


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'charity_donation/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.create_user(email=email, password=password,
                                            first_name=first_name, last_name=last_name)

            return redirect('login')
        else:
            return render(request, 'charity_donation/register.html', {'form': form})
