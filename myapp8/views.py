from django.shortcuts import render

# Create your views here.


def show_home(request):
    return render(request, "view.html")


def show_details(request, id):
    return render(request, "view.html", {"id": id})
