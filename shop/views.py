import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from types import SimpleNamespace
from shop.models import Product, Image, Group, Category, Comments, Attribute, AttributeValue, ProductAttribute
from shop.serializer import ProductModelSerializer, ImageModelSerializer, GroupModelSerializer, \
    CategoryModelSerializer, AttributesModelSerializer, AttributesValueModelSerializer, \
    ProductsAttributesModelSerializer, CommentModelSerializer, OrderModelSerializer


class SubmitOrder(APIView):
    def post(self, request):
        serializer = OrderModelSerializer(data=request.data)
        # x = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d))
        # # request.data
        # items = x.items
        # request.data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmitComment(APIView):
    def post(self, request):
        serializer = CommentModelSerializer(data=request.data)
        # serializer.data.
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Search(APIView):
    def get(self, request, search_text):
        query = Product.objects.filter(name__contains=search_text, inventory__gt=0)
        serializer = ProductModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetProductAttributes(APIView):
    def get(self, request, product_key):
        query = Product.objects.get().productattribute_set.all()
        # ProductAttribute.objects.filter(product_id=product_key)
        serializer = ProductsAttributesModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetGroups(APIView):
    def get(self, request):
        query = Group.objects.all()
        serializer = GroupModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetCategorys(APIView):
    def get(self, request, group_key):
        query = Category.objects.filter(group=Group.objects.get(pk=group_key))
        serializer = CategoryModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetSpecialDiscount(APIView):
    def get(self, request):
        query = Product.objects.filter(specialDiscount=True, inventory__gt=0)
        serializer = ProductModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def getAll(request):
#     query = Product.objects.all().order_by('-crate_date')
#     serializer = ModelProductSerializer(query, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


class GetProductsByCategory(APIView):
    def get(self, request, category_id):
        query = Product.objects.filter(category_id=category_id, inventory__gt=0)
        serializer = ProductModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(ModelProductSerializer(Product.objects.all(), many=True).data, status=status.HTTP_200_OK)


class GetSameProducts(APIView):
    def get(self, request, product_id):
        # TODO Change the way similar products are offered
        query = Product.objects.filter(category_id=Product.objects.get(pk=product_id).category_id, inventory__gt=0)
        serializer = ProductModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(ModelProductSerializer(Product.objects.all(), many=True).data, status=status.HTTP_200_OK)


class GetAllProducts(APIView):
    def get(self, request):
        query = Product.objects.filter(inventory__gt=0)
        serializer = ProductModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(ModelProductSerializer(Product.objects.all(), many=True).data, status=status.HTTP_200_OK)


class GetProduct(APIView):
    def get(self, request, key):
        query = Product.objects.get(pk=key)
        serializer = ProductModelSerializer(query, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetImages(APIView):
    def get(self, request, key):
        # serializer = ModelImageSerializer(data=request.data)
        query = Image.objects.filter(product_id=key)

        image_serializer = ImageModelSerializer(query, many=True, context={'request': request})
        return Response(image_serializer.data, status=status.HTTP_200_OK)


class GetComments(APIView):
    def get(self, request, key):
        query = Comments.objects.filter(product_id=key)
        serializer = CommentModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateData(APIView):
    def get(self, request, key):
        query = Product.objects.get(pk=key)
        serializer = ProductModelSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, key):
        query = Product.objects.get(pk=key)
        serializer = ProductModelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InsertProduct(APIView):
    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#
# class Serach(APIView):
#     def get(self, request):
#         search = request.GET['name']
#         query = Product.objects.filter(name__contains=search)
#         serializer = ProductModelSerializer(query, many=True)
#
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     # return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


class Delete(APIView):
    def delete(self, request, pk):
        query = Product.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
