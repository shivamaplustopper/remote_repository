"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base_view),
    path('home',views.home_view),
    path('banglore',views.banglore_view),
    path('hyderabad',views.hyderabad_view),
    path('pune',views.pune_view),
    path('chennai',views.chennai_view),
    path('registration',views.registration_view),
    path('login',views.login_view),
]