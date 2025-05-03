from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.



def registration_view(request):
    return render(request,'user/signup.html')


def login_view(request):
    return render(request,'user/login.html')