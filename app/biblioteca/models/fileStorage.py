from django.db import models 

class FileStorage(models.Model):
    app_label = 'biblioteca'
    db_table = 'FileStorage'
    filePath = models.CharField(max_length=254,unique=True)
    virtualName = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)