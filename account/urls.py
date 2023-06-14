#selfmade
#pasted from urls and edited

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
#
from . import views



urlpatterns = [
   path("register/",views.user_register),
   path("login/",views.user_login),
   path("dashboard/",views.admin_dashboard),
   path("logout/",views.user_logout),
]