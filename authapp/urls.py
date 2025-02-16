from django.urls import path
from authapp import views

urlpatterns = [
    path("signup/", views.sign_up),
]
