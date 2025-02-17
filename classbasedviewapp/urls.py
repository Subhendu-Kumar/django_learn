from django.urls import path
from classbasedviewapp import views

urlpatterns = [
    path("clsview/", views.my_view.as_view()),
    path("renderview/", views.render_view, {"template_name": "view1.html"}),
    path("renderview2/", views.render_view, {"template_name": "view2.html"}),
    path("rendertemp1/", views.render_view_cls.as_view(template_name="view1.html")),
    path("rendertemp2/", views.render_view_cls.as_view(template_name="view2.html")),
    path("temp/", views.my_template_view.as_view()),
    # path("redirect/", views.my_redirect_view.as_view()),
    path("redirect/", views.my_redirect_view.as_view(url="https://youtube.com")),
]
