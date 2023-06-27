from django.contrib import admin
from .models import Book, BookFile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin list view
    list_display = ('id', 'title', 'author', 'category', 'trending')

    # Add search functionality based on specified fields
    search_fields = ('title', 'author', 'publisher')

    # Enable filtering by specified fields
    list_filter = ('published_date', 'publisher')

class BookFileAdmin(admin.ModelAdmin):
    list_display = ['book', 'format', 'link']  # Customize the displayed fields in the admin list view

    # Optional: Customize the fields displayed in the edit view
    fields = ['book', 'format', 'link']

    # Optional: Customize the search fields
    search_fields = ['book__title', 'format']

    # Optional: Customize the filters in the right sidebar
    list_filter = ['format']

admin.site.register(BookFile, BookFileAdmin)
