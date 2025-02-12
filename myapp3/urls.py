from django.urls import path
from myapp3 import views

urlpatterns = [
    # path("", views.my_view),
    path("", views.hello_by_name),
    path("display", views.display),
]
