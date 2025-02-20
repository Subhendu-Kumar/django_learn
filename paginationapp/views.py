from django.shortcuts import render
from paginationapp.models import book
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from django.http import Http404

# Create your views here.


def page_view(request):
    all_pages = book.objects.all()
    page = Paginator(all_pages, 2)
    page_num = request.GET.get("page")
    page_obj = page.get_page(page_num)
    return render(request, "view.html", {"page_obj": page_obj})


class page_list_cls(ListView):
    model = book
    template_name = "view.html"
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        try:
            return super(page_list_cls, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs["page"] = 1
            return super(page_list_cls, self).get_context_data(*args, **kwargs)


class page_details_cls(DetailView):
    model = book
    template_name = "view.html"