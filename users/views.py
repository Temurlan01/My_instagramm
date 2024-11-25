from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class UserRegistrationView(TemplateView):
    template_name = 'sign_up.html'


class MakeUserRegistrationView(View):

    def post(self, request, *args, **kwargs):

        return render(request, 'login.html')