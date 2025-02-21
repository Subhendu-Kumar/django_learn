from django.shortcuts import render
from querysetapiapp2.models import teacher, student

# Create your views here.


def v1(request):
    stu = student.objects.values_list("id", "name", named=True)
    ter = teacher.objects.values_list("id", "name", named=True)
    # data = stu.union(ter)
    # data = stu.union(ter, all=True)
    # data = stu.intersection(ter)
    # data = stu.difference(ter)
    # data = student.objects.filter(age=20) & student.objects.filter(name="suman")
    # data = student.objects.filter(age=20) | student.objects.filter(name="suman")
    data = student.objects.all()
    return render(request, "view.html", {"mydata": data})
