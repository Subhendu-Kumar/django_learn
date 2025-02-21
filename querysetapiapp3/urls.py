from django.urls import path
from querysetapiapp3 import views

urlpatterns = [path("", views.v1),path("v2/", views.v2)]
