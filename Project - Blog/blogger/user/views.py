from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.contrib.auth import login

def registration_view(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        fm = UserCreationForm(request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            fm.save()
            return redirect('/login')
        else:
            # print(fm.errors)
            context = {"form": fm}
            return render(request, 'user/signup.html', context=context)
    else:
        fm = UserCreationForm()
        context = {"form": fm}
        return render(request, 'user/signup.html', context=context)


def login_view(request):
    # print(request.method)
    if request.method == "POST":
        print(request.POST)
        fm = AuthenticationForm(data=request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            user = fm.get_user()
            login(request,user)
            return redirect('/')
        else:
            context = {"form": fm}
            print(fm.errors)
            return render(request, 'user/login.html', context=context)
    else:
        fm = AuthenticationForm()
        context = {"form": fm}
        return render(request, 'user/login.html', context=context)
