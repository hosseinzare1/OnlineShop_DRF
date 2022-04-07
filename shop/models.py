from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
from users_api.models import User


# Create your models here.
# Group -> Category -> Product -> Image

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    imageUrl = models.ImageField(upload_to='images/', null=True)
    price = models.CharField(max_length=16, blank=True)
    fav = models.BooleanField()
    discount = models.IntegerField(default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])
    specialDiscount = models.BooleanField(default=False)
    crate_date = models.DateTimeField(default=datetime.now)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

#
# class SpecialDiscount(models.Model):
#     id = models.AutoField(primary_key=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    imageUrl = models.ImageField(upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.imageUrl.name


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128)
    text = models.TextField()

    class score(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    rating = models.IntegerField(choices=score.choices)

    user_number = models.ForeignKey(User, on_delete=models.CASCADE, to_field="number", null=True, blank=True)
    user_name = models.CharField(max_length=64)


class Attribute(models.Model):  # List of available Attributes
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    # content = models.ForeignKey(AttributeValues, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):  # list of available attribute values for each attributes
    id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.value


class ProductAttribute(models.Model):  # Table of Products Attributes with values
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(to=Attribute, to_field="name", on_delete=models.CASCADE)
    # on_delete=models.CASCADE,

    # default=1

    attribute_value = models.ForeignKey(to=AttributeValue, to_field="value", on_delete=models.CASCADE)
    # on_delete=models.CASCADE,
    #
    # limit_choices_to={'attribute': 1}

    #
    # attribute_c = Attribute.objects.get(id=type(attribute))
    # attribute_value_c = AttributeValue.objects.get(id=attribute_value.id)
