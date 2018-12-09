from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('oauth2_provider.urls', namespace='oauth')),
    path('auth/admin/', admin.site.urls),
]
