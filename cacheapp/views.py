from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.


# @cache_page(30) also can be used in urls.py file
def v1(request):
    return render(request, "view.html")


def v2(request):
    return render(request, "view.html")


def v3(request):
    return render(request, "view.html")
