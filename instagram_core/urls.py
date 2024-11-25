
from django.contrib import admin
from django.urls import path

from users.views import UserRegistrationView, MakeUserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrations/', UserRegistrationView.as_view(), name='registrations-url'),
    path('make-registration', MakeUserRegistrationView.as_view(), name='make-registration-url')
]
