from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def v1(request):
    return HttpResponse("this is my 1st view!!!! myapp")


def v2(request):
    return HttpResponse("this is my 2nd view!!!! myapp")
