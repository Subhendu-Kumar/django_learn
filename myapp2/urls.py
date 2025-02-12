from django.urls import path
from myapp2 import views

urlpatterns = [
    # path("", views.my_view),
    path("", views.hello_by_name)
]
