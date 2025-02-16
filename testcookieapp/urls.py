from django.urls import path
from testcookieapp import views

urlpatterns = [
    path("set/", views.set_session),
    path("check/", views.check_session),
    path("del/", views.del_session),
]
