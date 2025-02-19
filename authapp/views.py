from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import sign_up_form, edit_user_data_form
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = sign_up_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User created successfully!")
            return HttpResponseRedirect("/signin/")
        else:
            messages.info(request, "Please enter valid details.")
    else:
        fm = sign_up_form()

    return render(request, "view.html", {"form": fm})


def sign_in(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            pwd = fm.cleaned_data["password"]
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/profile/")
            else:
                messages.info(request, "credentials not matched!!")
        else:
            messages.info(request, "Please enter valid credentials!")
    else:
        fm = AuthenticationForm()

    return render(request, "view.html", {"form": fm})


def signout(request):
    logout(request)
    return HttpResponseRedirect("/signin/")


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = edit_user_data_form(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, "profile updated successfully!")
        else:
            fm = edit_user_data_form(instance=request.user)
        return render(request, "view.html", {"name": request.user, "form": fm})
    else:
        return HttpResponseRedirect("/signin/")


def change_password_with_old_password(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, "password changed successfully!")
            return HttpResponseRedirect("/profile/")
        else:
            messages.error(request, "in valid form data!")
    else:
        fm = PasswordChangeForm(user=request.user)

    return render(request, "view.html", {"form": fm})


def change_password_without_old_password(request):
    if request.method == "POST":
        fm = SetPasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, "password changed successfully!")
            return HttpResponseRedirect("/profile/")
        else:
            messages.error(request, "in valid form data!")
    else:
        fm = SetPasswordForm(user=request.user)

    return render(request, "view.html", {"form": fm})
