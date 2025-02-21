from django.shortcuts import render
from querysetapiapp3.models import student
from django.db.models import Avg, Max, Min, Count, Sum

# Create your views here.


def v1(request):
    # std = student.objects.all()
    # std = student.objects.filter(name__exact="Subhendu kumar")
    # std = student.objects.filter(name__iexact="subhendu kumar")
    # std = student.objects.filter(name__contains="kumar")
    # std = student.objects.filter(id__in=[2,3])
    # std = student.objects.filter(marks__gt=475)
    # std = student.objects.filter(marks__gte=475)
    # std = student.objects.filter(marks__lt=518)
    # std = student.objects.filter(marks__lte=518)
    # std = student.objects.filter(id__range=[1,3])
    # std = student.objects.filter(date_admited__year=2025)
    # std = student.objects.filter(date_admited__month__gt=2)
    # std = student.objects.filter(date_admited__month__gte=2)
    # std = student.objects.filter(date_passed__week=5)
    # std = student.objects.filter(date_passed__week__day=5)
    std = student.objects.filter(date_admited__quarter=1)
    return render(request, "view.html", {"std_data": std})


def v2(request):
    std = student.objects.all()
    avg_marks = std.aggregate(Avg("marks"))
    total_marks = std.aggregate(Sum("marks"))
    max_marks = std.aggregate(Max("marks"))
    min_marks = std.aggregate(Min("marks"))
    total_count = std.aggregate(Count("marks"))
    context = {
        "std_data": std,
        "analytics_std": {
            "avg_marks": avg_marks,
            "total_marks": total_marks,
            "max_marks": max_marks,
            "min_marks": min_marks,
            "count": total_count,
        },
    }
    print(context)
    return render(request, "view.html", context)
