from django.contrib import admin
from users_api import models


class AdminMode(admin.ModelAdmin):
    list_display = ['name', 'number', 'created_at']
    search_fields = ['name', 'number']


admin.site.register(models.User, AdminMode)

# Register your models here.
