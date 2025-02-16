from django.shortcuts import render
from authapp.forms import sign_up_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = sign_up_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User created successfully!")
        else:
            messages.info(request, "Please enter valid details.")
    else:
        fm = sign_up_form()

    return render(request, "signup.html", {"form": fm})


def sign_in(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.data)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            pwd = fm.cleaned_data["password"]
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
            else
            messages.success(request, "User created successfully!")
        else:
            messages.info(request, "Please enter valid details.")
    else:
        fm = AuthenticationForm()

    return render(request, "signin.html", {"form": fm})
