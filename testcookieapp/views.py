from django.shortcuts import render

# Create your views here.


def set_session(request):
    request.session.set_test_cookie()
    return render(request, "view.html")


def check_session(request):
    if request.session.set_test_cookie():
        print("users browser allow accepting cookie")
    else:
        print("user has disabled cookies")
    return render(request, "view.html")


def del_session(request):
    request.session.delete_test_cookie()
    return render(request, "view.html")
