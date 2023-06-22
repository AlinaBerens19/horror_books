from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin list view
    list_display = ('id', 'title', 'author', 'category', 'trending')

    # Add search functionality based on specified fields
    search_fields = ('title', 'author', 'publisher')

    # Enable filtering by specified fields
    list_filter = ('published_date', 'publisher')
