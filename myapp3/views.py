from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_by_name(request):
    return render(request, "index.html")


def display(request):
    name = request.POST["name"]
    password = request.POST["password"]
    return render(request, "display.html", {"name": name, "password": password})
