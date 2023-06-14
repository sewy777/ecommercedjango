from django.shortcuts import render,redirect
#render=show/visual
#no '/' in render

#redirect=page ma redirect
# '/' needed in redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .auth import admin_only



# Create your views here.

def user_register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"User Registered Successfully")
            return redirect("/register")
        else:
            messages.add_message(request,messages.ERROR,"User Register Unsuccessfull, Please Try Again")
            return render(request,"accounts/register.html",{
            # "form":UserCreationForm or "form":form
                "form":form
        })
    
    context={
        "form":UserCreationForm
    }
    return render(request,"accounts/register.html",context)

def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],
            password=data['password'])
            if user is not None:
                login(request,user)
                # login garepachi dashboard page kholne
                return redirect("/dashboard")
            else:
                messages.add_message(request,messages.ERROR,"User Not Verified")
                return render(request,"accounts/login.html",{
                    "form":form
                })
    
    
    context={
        "form":LoginForm
    }
    # context kei pathauna paryo bhani
    return render(request,"accounts/login.html",context)

# login na bhaye sama "/dashboard" garda dashboard page dekhaudaina
@login_required
@admin_only
# github copy gareko dashboard
def admin_dashboard(request):
    return render(request,"accounts/dashboard.html")

def user_logout(request):
    logout(request)
    return redirect("/login")