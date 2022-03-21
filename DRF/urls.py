from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from allauth.account.views import ConfirmEmailView
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Email Verified Successfully!")

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
        user = get_user_model().objects.get(email=self.object.email_address.email)
        redirect_url = reverse('home')
        return redirect(redirect_url)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    #restauthtoken urls
    #path('auth/', include('rest_authtoken.urls')),
    #path('api/', include('accounts.urls')),

    #rest-auth urls
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/account-confirm-email/(?P<key>.+)/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),

]
