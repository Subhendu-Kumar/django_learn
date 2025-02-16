from django.shortcuts import render, HttpResponse
from django.views import View
from classbasedviewapp.forms import myForm

# Create your views here.


class my_view(View):
    def get(self, request):
        fm = myForm()
        return render(request, "cls.html", {"form": fm})
