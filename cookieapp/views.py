from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta, timezone

# Create your views here.


def set_cookie(request):
    res = HttpResponse("cookie is set all done!")
    # res.set_cookie("sk", "Subhendu kumar dutta")
    # res.set_cookie("sk", "Subhendu kumar dutta", max_age=10)
    res.set_cookie(
        "sk",
        "Subhendu kumar dutta",
        expires=(datetime.now(timezone.utc) + timedelta(days=4)),
    )
    return res


def get_cookie(request):
    # cookie_val = request.COOKIES["sk"]
    cookie_val = request.COOKIES.get("sk", "no cookie data available")
    return HttpResponse("cookie data is : " + cookie_val)


def del_cookie(request):
    res = HttpResponse("cookie deleted")
    res.delete_cookie("sk")
    return res
