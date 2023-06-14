"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#copypasted in account urls
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my first Django page")

def home(request):
    return HttpResponse("This is home page")


urlpatterns = [
    path('a/', admin.site.urls),
    # this is my first django page
    # path("",index),
    path("home/",home),
    path("admin/", include("demo_app.urls")),
    
    path("",include("account.urls")),
    # after adding users in setting.py'installed apps' now we can add users url.py
    path("",include("users.urls"))
    

]
