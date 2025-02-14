from django.shortcuts import render

# Create your views here.


def show_home(request):
    return render(request, "dishome.html")


def show_details(request, id):
    return render(request, "display2.html", {"id": id})
