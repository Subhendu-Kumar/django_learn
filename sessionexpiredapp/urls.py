from django.urls import path
from sessionexpiredapp import views

urlpatterns = [
    path("set/", views.set_session),
    path("get/", views.get_session),
]
