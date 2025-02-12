from django.urls import path
from myapp4 import views

urlpatterns = [
    path("", views.student_view),
    path("byid/<int:id>", views.get_student_by_id),
]
