from urllib import request
from django.contrib.auth import login
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class UserRegistrationView(TemplateView):
    template_name = 'sign_up.html'


class MakeUserRegistrationView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        print('это то что ', data)
        first_name = data['first_name'],
        last_name = data['last_name'],
        username = data['username'],
        password = data['password']
        user = CustomUser.objects.create_user(
            nickname=username,password=password,
            first_name=first_name, last_name=last_name,
        )
        return render(request, 'login.html')


class LoginListView(TemplateView):
    template_name = 'login.html'


class MakeLoginView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        nickname = data['username'],
        password = data['password']

        user = CustomUser.objects.get(nickname=nickname)
        print('Пользователь', user)
        correct = user.check_password(password)
        print('коррект равен', correct)
        if correct == True:
            login(request, user)
            return render(request, 'home.html', context={'logged_in': True})
        else:
            return render(request, 'login.html', context={'logged_in': False})


class HomeView(TemplateView):
    template_name = 'home.html'