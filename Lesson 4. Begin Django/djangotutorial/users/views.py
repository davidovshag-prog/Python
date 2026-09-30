from django.shortcuts import render
from django import forms

# Create your views here.
def user_login(request):
    form = CustomUserLoginForm()
    return render("login.html", {"form": form})

def user_register(request):
    return render(request, "register.html")