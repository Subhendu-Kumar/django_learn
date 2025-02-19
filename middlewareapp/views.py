from django.shortcuts import render, HttpResponse

# Create your views here.


def v1(request):
    print("this is v1 view!")
    return HttpResponse("this is my first middleware test!")