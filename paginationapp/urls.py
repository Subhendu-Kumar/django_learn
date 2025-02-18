from django.urls import path
from paginationapp import views

urlpatterns = [
    path("pagefun/", views.page_view),
    path("pagecls/", views.page_list_cls.as_view()),
    path("detailcls/<int:pk>", views.page_details_cls.as_view(), name="details"),
]
