from django.contrib import admin
from modelrelationshipapp.models import new_book, post, dance

# Register your models here.


@admin.register(new_book)
class new_book_admin(admin.ModelAdmin):
    list_display = ["book_name", "book_author", "book_published_date", "user"]


@admin.register(post)
class post_admin(admin.ModelAdmin):
    list_display = ["post_title", "post_category", "post_published_date", "user"]


@admin.register(dance)
class dance_admin(admin.ModelAdmin):
    list_display = ["dance_name", "dance_type", "dance_by"]
