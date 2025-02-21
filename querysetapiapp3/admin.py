from django.contrib import admin
from querysetapiapp3.models import student

# Register your models here.


@admin.register(student)
class student_admin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "branch",
        "address",
        "marks",
        "age",
        "date_admited",
        "date_passed",
    ]
