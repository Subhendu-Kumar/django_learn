from django.shortcuts import render

# Create your views here.


def set_session(request):
    request.session["skop"] = "skopisbest"
    return render(request, "set.html")


def get_session(request):
    # value = request.session["skop"]
    value = request.session.get("skop", "no session id found")
    age = request.session.get_expiry_age()
    date = request.session.get_expiry_date()
    return render(request, "get.html", {"value": value, "age": age, "date": date})


def del_session(request):
    # if "skop" in request.session:
    #     del request.session["skop"]
    request.session.flush()
    print(request.session.get_expire_at_browser_close())
    return render(request, "del.html")
