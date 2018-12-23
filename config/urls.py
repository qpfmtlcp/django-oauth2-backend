from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login',
         kwargs={'template_name': 'templates/login.html'}),
    path('', include('oauth2_provider.urls', namespace='oauth')),
]
