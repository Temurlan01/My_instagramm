from django.shortcuts import render
from django.views.generic import TemplateView

from publications.models import Publication
from users.models import CustomUser

class HomeView(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, *args, **kwargs):
        context = {
            'publication': Publication.objects.all(),
        }
        return context

