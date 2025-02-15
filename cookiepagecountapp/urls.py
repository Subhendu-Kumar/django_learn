from django.urls import path
from cookiepagecountapp import views

urlpatterns = [
    path("", views.count_page_view)
]
