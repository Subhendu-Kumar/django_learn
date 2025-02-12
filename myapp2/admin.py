from django.contrib import admin
from myapp2.models import Employee, Student

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "address", "age"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "branch", "email", "address", "age"]


# admin.site.register(Employee, EmployeeAdmin)
