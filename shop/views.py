from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

from shop.models import Product, Image
from shop.serializer import ModelProductSerializer, ModelImageSerializer


#
# @api_view(['GET'])
# def getAll(request):
#     query = Product.objects.all().order_by('-crate_date')
#     serializer = ModelProductSerializer(query, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllProducts(APIView):
    def get(self, request):
        query = Product.objects.all()
        serializer = ModelProductSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(ModelProductSerializer(Product.objects.all(), many=True).data, status=status.HTTP_200_OK)


class GetImages(APIView):
    def get(self, request):
        serializer = ModelImageSerializer(data=request.data)
        product_id = serializer.initial_data.get("id")
        query = Image.objects.filter(product=Product.objects.get(pk=product_id))

        image_serializer = ModelImageSerializer(query, many=True, context={'request': request})
        return Response(image_serializer.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
    def get(self, request):
        query = Product.objects.filter(fav=True)
        serializer = ModelProductSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateData(APIView):
    def get(self, request, key):
        query = Product.objects.get(pk=key)
        serializer = ModelProductSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, key):
        query = Product.objects.get(pk=key)
        serializer = ModelProductSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InsertProduct(APIView):
    def post(self, request):
        serializer = ModelProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Serach(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Product.objects.filter(name__contains=search)
        serializer = ModelProductSerializer(query, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    # return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


class Delete(APIView):
    def delete(self, request, pk):
        query = Product.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
