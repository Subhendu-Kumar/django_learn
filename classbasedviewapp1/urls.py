from django.urls import path
from classbasedviewapp1 import views

urlpatterns = [
    path("list/", views.list_view.as_view(template_name="subhendumodel_list.html")),
    path("list/<int:id>", views.details_view.as_view()),
    path("list1/", views.combine_view2.as_view()),
    path("list2/<int:pk>", views.combine_view1.as_view(), name="details"),
]
