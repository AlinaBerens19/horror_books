from django.contrib import admin

from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin list view
    list_display = ('id', 'username', 'name', 'created', 'email', 'phone')

    # Add search functionality based on specified fields
    search_fields = ('email', 'name', 'phone')

    # Enable filtering by specified fields
    list_filter = ('created', 'updated')

admin.site.register(Profile)    

