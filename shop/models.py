from django.db import models
from datetime import datetime


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    imageUrl = models.ImageField(upload_to='images/', null=True)
    fav = models.BooleanField()
    crate_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    imageUrl = models.ImageField(upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.imageUrl
