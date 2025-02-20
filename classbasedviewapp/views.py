from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from classbasedviewapp.forms import myForm

# Create your views here.


class my_view(View):
    def get(self, request):
        fm = myForm()
        return render(request, "view.html", {"form": fm})


# rendering multiple template using same view


def render_view(request, template_name):
    return render(request, template_name, {"msg": "my name is subhendu"})


class render_view_cls(View):
    template_name = ""

    def get(self, request):
        return render(request, self.template_name, {"msg": "you are bad boy"})


# working with template view


class my_template_view(TemplateView):
    template_name = "mytemp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Subhendu kumar"
        context["city"] = "Bhadrak, odisha"
        return context


# working with redirect view


class my_redirect_view(RedirectView):
    # url = "https://youtube.com"
    pass
