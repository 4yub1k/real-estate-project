from django.db import models
from datetime import datetime

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/blocks/%Y/%m/%d/',)
    def __str__(self):
        return self.title