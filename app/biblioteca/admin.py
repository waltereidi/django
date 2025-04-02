from django.contrib import admin

# Register your models here.
from biblioteca.models.book import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):  
    list_display = ('title', 'isbn')
    list_filter = ('title', 'isbn')
    search_fields = ('title', 'isbn')
    prepopulated_fields = {'description': ('title',)}
    date_hierarchy = 'updated'
    ordering = ('updated', 'created')