from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path("myapp1/", include("myapp1.urls")),
    path("myapp2/", include("myapp2.urls")),
    path("myapp3/", include("myapp3.urls")),
    path("myapp4/", include("myapp4.urls")),
    path("myapp5/", include("myapp5.urls")),
    path("myapp6/", include("myapp6.urls")),
    path("myapp7/", include("myapp7.urls")),
    path("", include("myapp8.urls")),
]
