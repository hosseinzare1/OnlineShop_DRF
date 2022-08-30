from unicodedata import name
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
from users_api.models import User

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    imageUrl = models.ImageField(upload_to='images/', null=True)
    price = models.CharField(max_length=16, blank=True)
    discount = models.IntegerField(default=0, validators=[
        MaxValueValidator(99),
        MinValueValidator(0)
    ])
    specialDiscount = models.BooleanField(default=False)
    crate_date = models.DateTimeField(default=datetime.now)
    group = models.ForeignKey(Group, to_field='name', related_name='products', on_delete=models.CASCADE, null=True,
                              blank=True)
    category = models.ForeignKey(Category, to_field='name', related_name='products', on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)

    inventory = models.IntegerField(null=True)

    # These two fields are not serialized
    initial_inventory = models.IntegerField(null=True)
    Number_of_items_sold = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='number', null=True)

    class Situations(models.Choices):
        Registered = 1
        Processing = 2
        Delivered_to_the_post_office = 3

    state = models.IntegerField(choices=Situations.choices, default=1)
    trackingNumber = models.IntegerField(default=1)

    submit_time = models.CharField(max_length=16, null=True)
    submit_date = models.CharField(max_length=16, null=True)

    gregorianDataTime = models.DateTimeField(auto_now_add=True, null=True)

    totalPrice = models.IntegerField(null=True)

    transferee_name = models.CharField(max_length=64, null=True)
    transferee_number = models.CharField(max_length=16, null=True)
    transferee_address = models.TextField(null=True)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100,null=True)
    imageUrl = models.CharField(max_length=256, null=True)

    quantity = models.IntegerField(default=1)
    unit_price = models.IntegerField(default=1)
    unit_discount = models.IntegerField(default=1)


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


class NewsImage(models.Model):
    id = models.AutoField(primary_key=True)
    imageUrl = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.imageUrl.name

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128)
    text = models.TextField()

    submit_time = models.CharField(max_length=16, null=True)
    submit_date = models.CharField(max_length=16, null=True)

    gregorianDataTime = models.DateTimeField(auto_now_add=True, null=True)

    class score(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    rating = models.IntegerField(choices=score.choices)

    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="number", null=True, blank=True)
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
