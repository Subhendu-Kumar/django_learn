from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.


# def my_view(request):
#     date = datetime.datetime.now()
#     return HttpResponse(date)
#     return render(request, "index.html", {"date": date})


def hello_by_name(request):
    return HttpResponse("hello")
