from django.urls import path, include
from crudmysqlapp import views

urlpatterns = [
    path("", views.v1),
    path("users/", views.show_all_users),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
]
