from django.shortcuts import render
from myapp6.forms import skForm
from myapp6.models import SkModel
from django.contrib import messages

# Create your views here.


def form_view(request):
    if request.method == "POST":
        fm = skForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            addrress = fm.cleaned_data["address"]
            age = fm.cleaned_data["age"]
            sk = SkModel(name=name, email=email, address=addrress, age=age)
            sk.save()
            messages.add_message(request, messages.SUCCESS, "Data inserted successfully.")
        else:
            messages.info(request, "Enter valid data.")
    else:
        fm = skForm()
    return render(request, "view.html", {"form": fm})
