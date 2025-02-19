from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def count_page_view(request):
    if "count" in request.COOKIES:
        newcount = int(request.COOKIES["count"]) + 1
    else:
        newcount = 1
    res = render(request, "view.html", {"count": newcount})
    res.set_cookie("count", newcount)
    return res
