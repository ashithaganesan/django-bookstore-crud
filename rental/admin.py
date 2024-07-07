from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("book_name",)}
    list_filter = ("author_name", "rating",)
    list_display = ("book_name", "author_name", "rating", "status")

admin.site.register(Book, BookAdmin)