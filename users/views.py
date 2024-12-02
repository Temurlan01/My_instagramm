from urllib import request
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser
from publications.models import Publication


class UserRegistrationView(TemplateView):
    template_name = 'sign_up.html'


class MakeUserRegistrationView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
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
        nickname = data['nickname']
        password = data['password']

        user = CustomUser.objects.get(nickname=nickname)
        correct = user.check_password(password)
        if correct == True:
            login(request, user)
            return redirect('home-url')
        else:
            return render(request, 'login.html', context={'logged_in': False})



class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        user = CustomUser.objects.get(id=kwargs['pk'])
        followers_count = user.my_followers.all().count()
        following_count = user.my_following.all().count()
        publications_count = user.my_publications.all().count()
        post = user.my_publications.all()
        context = {
            'user': user,
            'post': post,
            'followers_count': followers_count,
            'following_count': following_count,
            'publications_count': publications_count,

        }
        return context






