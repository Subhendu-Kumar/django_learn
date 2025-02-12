from django.contrib import admin
from myapp4.models import newStudent

# Register your models here.


@admin.register(newStudent)
class newStudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "address", "age"]
