from django.db import models
from datetime import datetime


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    fav = models.BooleanField()
    crate_date = models.DateTimeField(default=datetime.now)

def __str__(self):
    return self.name
