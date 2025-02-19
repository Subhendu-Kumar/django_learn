from django.shortcuts import render

# Create your views here.


def page_count_view(request):
    count = request.session.get("count", 0)
    new_count = count + 1
    request.session["count"] = new_count
    return render(request, "view.html", {"count": count})
