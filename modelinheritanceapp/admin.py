from django.contrib import admin
from modelinheritanceapp.models import university, college

# Register your models here.


@admin.register(university)
class universityAdmin(admin.ModelAdmin):
    list_display = ["id", "uname", "ulocation"]


@admin.register(college)
class collegeAdmin(admin.ModelAdmin):
    list_display = ["id", "uname", "ulocation"]