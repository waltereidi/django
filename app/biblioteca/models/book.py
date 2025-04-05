from django.db import models


class Book(models.Model):
    app_label = 'biblioteca'
    db_table = 'book'
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
def __str__(self):
    return self.title
def teste():
    return 'sdsd'

