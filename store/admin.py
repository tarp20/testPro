from django.contrib import admin

from .views import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass 