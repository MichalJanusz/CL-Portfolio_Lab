from django.shortcuts import render

from .models import *
from django.views import View

# Create your views here.


class LandingPageView(View):
    def get(self, request):
        bags_count = 0
        donations = Donation.objects.all()
        for donation in donations:
            bags_count += donation.quantity
        institutions_count = len(Institution.objects.all())
        foundations = Institution.objects.filter(type=1)
        organisations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        ctx = {'bags_count': bags_count, 'institutions_count': institutions_count, 'foundations': foundations,
               'organisations': organisations, 'local_collections': local_collections}
        return render(request, 'charity_donation/index.html', ctx)


class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity_donation/form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'charity_donation/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'charity_donation/register.html')
