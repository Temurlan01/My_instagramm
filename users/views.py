from urllib import request
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
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
        nickname = data['nickname'],
        password = data['password']

        user = CustomUser.objects.get(nickname=nickname)
        print('Пользователь', user)
        correct = user.check_password(password)
        print('коррект равен', correct)
        if correct == True:
            login(request, user)
            return redirect('home-url')
        else:
            return render(request, 'login.html', context={'logged_in': False})


class UserMakeLogoutView(View):
    def post(self, *args, **kwargs):
        logout(request)
        return render(request, 'login.html')


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = {
            'user': current_user,
        }
        return context


class MyProfilePageView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user

        followers_count = current_user.my_followers.all().count()
        following_count = current_user.my_following.all().count()

        publications_count = current_user.my_publications.all().count()

        context = {
            'followers_count': followers_count,
            'following_count': following_count,
            'publications_count': publications_count,
        }
        return context
