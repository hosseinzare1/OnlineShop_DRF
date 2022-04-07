from django.db import models
# from datetime import datetime
from django.utils import timezone


# import datetime



class User(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    number = models.IntegerField(blank=True, unique=True)
    password = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    address = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
