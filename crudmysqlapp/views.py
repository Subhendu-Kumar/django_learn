from django.shortcuts import render, HttpResponse, redirect
from crudmysqlapp import forms, models

# Create your views here.


def v1(request):
    if request.method == "POST":
        form = forms.user_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data inserted to user table!")
    else:
        form = forms.user_form()
    return render(request, "view.html", {"form": form, "user": None})


def show_all_users(request):
    users = models.user.objects.all()
    return render(request, "view.html", {"users": users, "user": None})


def delete(request, id):
    user = models.user.objects.get(id=id)
    user.delete()
    return redirect("/users/")


def edit(request, id):
    user = models.user.objects.get(id=id)
    return render(request, "view.html", {"user": user})


def update(request, id):
    user = models.user.objects.get(id=id)
    form = forms.user_form(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/users/")
    return render(request, "view.html", {"user": user})
