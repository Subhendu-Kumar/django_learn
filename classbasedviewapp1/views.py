from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from classbasedviewapp1.models import SubhenduModel

# Create your views here.


class list_view(ListView):
    model = SubhenduModel
    ordering = ["name"]
    context_object_name = "students"

    # def get_queryset(self):
    #     return SubhenduModel.objects.filter(age=21)


class details_view(DetailView):
    model = SubhenduModel
    template_name = "view.html"
    pk_url_kwarg = "id"
    context_object_name = "student"


class combine_view1(DetailView):
    model = SubhenduModel
    template_name = "view.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["student"] = self.model.objects.all()
        return context


class combine_view2(ListView):
    model = SubhenduModel
    template_name = "view.html"
    context_object_name = "students"
