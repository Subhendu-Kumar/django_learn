from django.contrib import admin
from myapp6.models import SkModel

# Register your models here.

@admin.register(SkModel)
class SkModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "address", "age"]
