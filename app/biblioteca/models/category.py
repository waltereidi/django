from django.db import models

class Category(models.Model):
    app_label = 'biblioteca'
    db_table = 'category'
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)
def __str__(self):
    return self.name


