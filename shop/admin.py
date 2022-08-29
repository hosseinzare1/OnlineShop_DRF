from django.contrib import admin
from shop import models


class AdminMode(admin.ModelAdmin):
    list_display = ['id','name', 'imageUrl']
    search_fields = ['name']


class ImageAdminMode(admin.ModelAdmin):
    list_display = ['id', 'product']
    search_fields = ['product']

class NewsImageAdminMode(admin.ModelAdmin):
    list_display = ['id','imageUrl']

class OrderAdminMode(admin.ModelAdmin):
    list_display = ['id', 'user']


class OrderItemAdminMode(admin.ModelAdmin):
    list_display = ['id', 'order', 'product']


#
# class SpecialDiscountAdminMode(admin.ModelAdmin):
#     list_display = ['id', 'product', 'discount']
#     search_fields = ['product']


class CommentAdminMode(admin.ModelAdmin):
    list_display = ['id', 'product', 'text']
    search_fields = ['text']


class GroupAdminMode(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class CategoryAdminMode(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class AttributeAdminMode(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class AttributeValueAdminMode(admin.ModelAdmin):
    list_display = ['id', 'value']
    search_fields = ['value']


class ProductAttributeAdminMode(admin.ModelAdmin):
    list_display = ['id', 'product', 'attribute', 'attribute_value']
    search_fields = ['attribute_value']


admin.site.register(models.Group, GroupAdminMode)
admin.site.register(models.Category, CategoryAdminMode)
admin.site.register(models.Product, AdminMode)
admin.site.register(models.Image, ImageAdminMode)
admin.site.register(models.NewsImage, NewsImageAdminMode)
# admin.site.register(models.SpecialDiscount, SpecialDiscountAdminMode)
admin.site.register(models.Comments, CommentAdminMode)

admin.site.register(models.Order, OrderAdminMode)
admin.site.register(models.OrderItem, OrderItemAdminMode)

admin.site.register(models.Attribute, AttributeAdminMode)
admin.site.register(models.AttributeValue, AttributeValueAdminMode)
admin.site.register(models.ProductAttribute, ProductAttributeAdminMode)
