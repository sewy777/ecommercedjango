from django.shortcuts import redirect 

#To check if the user is logged in or not
# view_function => kata pugaune
def authenticated_user(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function

def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect("/")
    return wrapper_function

def user_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return redirect("/dashboard")
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function

