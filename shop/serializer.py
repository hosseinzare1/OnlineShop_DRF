from rest_framework import serializers
from shop import models


# from django_jalali.serializers.serializerfield import JDateTimeField


#
# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     image = serializers.ImageField(use_url=True, null=True)
#     fav = serializers.CharField(max_length=2)

class OrderItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"


class OrderModelSerializer(serializers.ModelSerializer):
    # tracks = TrackSerializer(many=True)
    order_items = OrderItemModelSerializer(many=True)

    class Meta:
        model = models.Order
        fields = [
        "id",
        "user",
        
        "state",
        "trackingNumber",

        "order_items","totalPrice",        
        "submit_time","submit_date",

        "transferee_name","transferee_number","transferee_address",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')
        order = models.Order.objects.create(**validated_data)
        for item in items_data:
            models.OrderItem.objects.create(order=order, **item)
        return order


class ProductModelSerializer(serializers.ModelSerializer):
    # date_time = JDateTimeField()

    class Meta:
        model = models.Product
        fields = ['id', 'name', 'description', 'imageUrl', 'price', 'discount', 'specialDiscount', 'crate_date',
                  'category', 'group', 'inventory']

    def create(self, validated_data):
        product = models.Product.objects.create(**validated_data)

        group = product.group
        group.count = group.count + 1
        group.save()

        return product


#
# class SpecialDiscountModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.SpecialDiscount
#         fields = '__all__'


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
        
class NewsImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields = '__all__'


class CommentModelSerializer(serializers.ModelSerializer):
  ##  product = ProductModelSerializer(many=False)
    class Meta:
        model = models.Comments
        fields = '__all__'


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class AttributesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = '__all__'


class AttributesValueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttributeValue
        fields = '__all__'


class ProductsAttributesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductAttribute
        fields = '__all__'
