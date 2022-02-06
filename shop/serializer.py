from rest_framework import serializers
from shop import models

#
# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     image = serializers.ImageField(use_url=True, null=True)
#     fav = serializers.CharField(max_length=2)


class ModelProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
