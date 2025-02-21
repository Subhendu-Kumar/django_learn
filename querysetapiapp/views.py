from django.shortcuts import render
from querysetapiapp.models import my_model

# Create your views here.


def v1(request):
    per = my_model.objects.all()
    # per = my_model.objects.filter(age=20)
    # per = my_model.objects.exclude(age=20)
    # per = my_model.objects.order_by("age")
    # per = my_model.objects.order_by("-age")
    # per = my_model.objects.order_by("?")
    # per = my_model.objects.order_by("age").reverse()[1:3]
    # per = my_model.objects.values()
    # per = my_model.objects.values_list()
    print("Return Type: ", per)
    print("SQL query: ", per.query)
    return render(request, "view.html", {"person": per})
