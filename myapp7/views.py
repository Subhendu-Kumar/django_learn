from django.shortcuts import render
from myapp7.forms import myapp7Form
from myapp7.models import myapp7Model
from django.contrib import messages

# Create your views here.


def form_view(request):
    if request.method == "POST":
        fm = myapp7Form(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            addrress = fm.cleaned_data["address"]
            age = fm.cleaned_data["age"]
            sk = myapp7Model(name=name, email=email, address=addrress, age=age)
            sk.save()
            messages.add_message(
                request, messages.SUCCESS, "Data inserted successfully."
            )
        else:
            messages.info(request, "Enter valid data.")
    else:
        fm = myapp7Form()
    return render(request, "view.html", {"form": fm})
