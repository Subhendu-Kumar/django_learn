from django.shortcuts import render
from myapp4.models import newStudent

# Create your views here.


def student_view(request):
    stu = newStudent.objects.all()
    return render(request, "view.html", {"student2": stu})


def get_student_by_id(request, id):
    stu = newStudent.objects.get(pk=id)
    return render(request, "view.html", {"student3": stu})
