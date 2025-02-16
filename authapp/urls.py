from django.urls import path
from authapp import views

urlpatterns = [
    path("signup/", views.sign_up),
    path("signin/", views.sign_in),
    path("profile/", views.profile),
    path("signout/", views.signout, name="logout"),
    path(
        "changepassword/",
        views.change_password_with_old_password,
        name="changepassword",
    ),
    path(
        "changepassword2/",
        views.change_password_without_old_password,
        name="changepassword2",
    ),
]
