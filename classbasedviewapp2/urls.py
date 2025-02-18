from django.urls import path
from classbasedviewapp2 import views

urlpatterns = [
    path("success/", views.success.as_view()),
    path("nodelete/", views.nodelete.as_view(), name="nodelete"),
    path("form/", views.form_view.as_view()),
    path("create/", views.create_view.as_view()),
    path("update/<int:pk>", views.update_view.as_view()),
    path("delete/<int:pk>", views.delete_view.as_view()),
]
