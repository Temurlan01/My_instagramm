from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from users.views import UserRegistrationView, MakeUserRegistrationView, LoginListView, MakeLoginView, HomeView, \
    ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('registrations/', UserRegistrationView.as_view(), name='registrations-url'),
    path('make-registration/', MakeUserRegistrationView.as_view(), name='make-registration-url'),
    path('login/', LoginListView.as_view(), name='login-url'),
    path('make-login/', MakeLoginView.as_view(), name='make-login-url'),

    path('home/', HomeView.as_view(), name='home-url'),

    path('profile/', ProfileView.as_view(), name='profile')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
