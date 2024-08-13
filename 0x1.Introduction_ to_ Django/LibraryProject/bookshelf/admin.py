

# bookshelf/admin.py

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable search functionality on these fields
    search_fields = ('title', 'author')
    
    # Add filters for publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)

# Register your models here.
