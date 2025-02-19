from django.shortcuts import render
from myapp5.forms import employeeForm

# Create your views here.


def form_view(request):
    if request.method == "POST":
        fm = employeeForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data["name"])
            print(fm.cleaned_data["email"])
            print(fm.cleaned_data["city"])
            print(fm.cleaned_data["age"])
            print(fm.cleaned_data["password"])
            print(fm.cleaned_data["retypepassword"])
        else:
            print("form is not valid")
    else:
        fm = employeeForm()
    return render(request, "view.html", {"form": fm})
