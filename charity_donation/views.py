from django.shortcuts import render


from django.views import View
# Create your views here.


class LandingPageView(View):
    def get(self, request):
        return render(request, 'charity_donation/__base__.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity_donation/form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'charity_donation/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'charity_donation/register.html')
