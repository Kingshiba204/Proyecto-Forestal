from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from faenas.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('faenas.urls')),
]
