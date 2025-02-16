from django.urls import path
from sessionpagecountapp import views

urlpatterns = [
    path("count/", views.page_count_view),
]
