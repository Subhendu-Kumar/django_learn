from django.urls import path
from classbasedviewapp import views

urlpatterns = [
    path("", views.my_view.as_view()),
]
