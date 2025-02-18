from django.contrib import admin
from paginationapp.models import book

# Register your models here.


@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published"]
