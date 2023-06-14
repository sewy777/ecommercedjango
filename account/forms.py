from django import forms


# def LoginForm(request):
#     username:forms.CharField()
#     password:forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)