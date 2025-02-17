from django.contrib import admin
from classbasedviewapp1.models import SubhenduModel

# Register your models here.


@admin.register(SubhenduModel)
class SubhenduModelAdmin(admin.ModelAdmin):
    list_display = ["name", "branch", "father_name", "mother_name", "address", "age"]
