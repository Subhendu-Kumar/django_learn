from django.shortcuts import render

# Create your views here.


def v1(request):
    return render(request, "mycache.html")
