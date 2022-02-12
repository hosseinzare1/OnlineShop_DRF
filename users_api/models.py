from django.db import models
# from datetime import datetime
from django.utils import timezone


# import datetime


class User(models.Model):
    name = models.CharField(max_length=20, null=True)
    number = models.CharField(max_length=13)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
