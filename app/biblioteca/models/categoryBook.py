from django.db import models
from biblioteca.models.category import Category 
from biblioteca.models.book import Book

class CategoryBook(models.Model):
    app_label ='biblioteca'
    db_table ='categoryBook'
    category = models.ForeignKey(Category , on_delete=models.RESTRICT)
    book = models.ForeignKey(Book , on_delete=models.RESTRICT)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)
def __str__(self):
    return self.id