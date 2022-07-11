from datetime import datetime
from django.db import models
# Create your models here.

class Tasktable(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField()
    time = models.DateTimeField(default=datetime.now, blank=True) 
    mtime = models.DateTimeField(default=datetime.now, blank=True)