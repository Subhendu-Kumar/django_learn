from django.urls import path
from myapp8 import views

urlpatterns = [
    path("app8/", views.show_home, name="home"),
    path("app8/<id>", views.show_details, name="display"),
]
