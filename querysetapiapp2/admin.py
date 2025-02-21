from django.contrib import admin
from querysetapiapp2.models import student, teacher

# Register your models here.


@admin.register(student)
class student_admin(admin.ModelAdmin):
    list_display = ["name", "city", "age", "dob"]


@admin.register(teacher)
class teacher_admin(admin.ModelAdmin):
    list_display = ["name", "city", "age", "dob", "salary"]
