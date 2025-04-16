from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    app_label = 'biblioteca'
    db_table = 'book'
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)
    user =  models.ForeignKey(User , on_delete=models.RESTRICT)
    active = models.BooleanField(default=1)
def __str__(self):
    return self.title