from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from classbasedviewapp2.forms import SuForm
from classbasedviewapp2.models import SuModel

# Create your views here.


class form_view(FormView):
    template_name = "formview.html"
    form_class = SuForm
    success_url = "/success/"

    def form_valid(self, form):
        print(form.cleaned_data["name"])
        print(form.cleaned_data["city"])
        print(form.cleaned_data["email"])
        print(form.cleaned_data["age"])
        return super().form_valid(form)


class create_view(CreateView):
    model = SuModel
    template_name = "formview.html"
    fields = "__all__"
    success_url = "/success/"


class update_view(UpdateView):
    model = SuModel
    template_name = "formview.html"
    fields = "__all__"
    success_url = "/success/"


class delete_view(DeleteView):
    model = SuModel
    template_name = "confirm.html"
    success_url = "/success/"


class success(TemplateView):
    template_name = "success.html"


class nodelete(TemplateView):
    template_name = "nodelete.html"
