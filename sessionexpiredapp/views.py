from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def set_session(request):
    request.session["skop"] = "skopisbest"
    return HttpResponse("session set success!")


def get_session(request):
    if "skop" in request.session:
        value = request.session["skop"]
        return render(request, "view.html", {"value": value})
    else:
        return HttpResponse("session has expired")