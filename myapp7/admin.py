from django.contrib import admin
from myapp7.models import myapp7Model

# Register your models here.


@admin.register(myapp7Model)
class myapp7ModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "address", "age"]
