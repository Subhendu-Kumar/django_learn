from django.contrib import admin
from querysetapiapp.models import my_model

# Register your models here.


@admin.register(my_model)
class my_model_admin(admin.ModelAdmin):
    list_display = ["name", "city", "age", "dob"]
