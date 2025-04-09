from django.contrib import admin

# Register your models here.
from biblioteca.models.book import Book
from biblioteca.models.category import Category
from biblioteca.models.categoryBook import CategoryBook
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):  
    list_display = ('title', 'isbn')
    list_filter = ('title', 'isbn')
    search_fields = ('title', 'isbn')
    prepopulated_fields = {'description': ('title',)}
    date_hierarchy = 'updated'
    ordering = ('updated', 'created')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'description')
    list_filter = ('name','description')
    search_field = ('name' , 'description')
    date_hierarchy = 'updated'
    ordering = ('updated', 'created')

@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin): 
    ordering = ('updated', 'created')
    list_display = ('category' , 'book')
    