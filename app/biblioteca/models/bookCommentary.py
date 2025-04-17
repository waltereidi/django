from django.db import models
from django.contrib.auth.models import User
from biblioteca.models.book import Book

class BookCommentary(models.Model):
    app_label = 'biblioteca'
    db_table = 'book'
    description = models.TextField()
    book = models.ForeignKey(Book , on_delete=models.RESTRICT)
    user =  models.ForeignKey(User , on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)
def __str__(self):
    return self.user