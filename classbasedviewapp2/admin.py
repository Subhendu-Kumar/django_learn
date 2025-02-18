from django.contrib import admin
from classbasedviewapp2.models import SuModel

# Register your models here.


@admin.register(SuModel)
class SuModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "city", "age"]
