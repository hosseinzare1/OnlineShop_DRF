from django.contrib import admin
from shop import models


class AdminMode(admin.ModelAdmin):
    list_display = ['name', 'imageUrl']
    search_fields = ['name']


class ImageAdminMode(admin.ModelAdmin):
    list_display = ['id', 'product']
    search_fields = ['product']


admin.site.register(models.Product, AdminMode)
admin.site.register(models.Image, ImageAdminMode)
