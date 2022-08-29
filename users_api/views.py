from django.shortcuts import render
from django.views.static import serve
from rest_framework.views import APIView
from rest_framework.response import Response
from users_api import status
from users_api.serializer import UserModelSerializers
from users_api.models import User


class GetAccountDetails(APIView):
    def get(self, request, number):
        query = User.objects.get(number=number)
        serializer = UserModelSerializers(query)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateAccount(APIView):
    def post(self, request, number):
        query = User.objects.get(number=number)
        serializer = UserModelSerializers(query, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_220_DATA_NOT_VALID)


class Login(APIView):
    def post(self, request):
        serializers = UserModelSerializers(data=request.data)
        number = serializers.initial_data.get('number')
        password = serializers.initial_data.get('password')
        serializers.is_valid()
        # if serializers.is_valid():
        query_number = User.objects.filter(number=number).count()
        if query_number > 0:
            query_number_password = User.objects.filter(number=number, password=password).count()
            if query_number_password > 0:
                # serializers.save()
                query = User.objects.get(number=number)
                userSerializer = UserModelSerializers(query)
                return Response(userSerializer.data, status=status.HTTP_212_LOGIN_SUCCESSFUL)
            else:
                return Response(serializers.data, status=status.HTTP_214_PASSWORD_WRONG)
        else:
            return Response(serializers.data, status=status.HTTP_213_THERE_IS_NO_ACCOUNT)
    # else:
    #     return Response(serializers.errors, status=status.HTTP_220_DATA_NOT_VALID)


class Signup(APIView):
    def post(self, request):
        serializers = UserModelSerializers(data=request.data)

        number = serializers.initial_data.get('number')

        query_number = User.objects.filter(number=number).count()
        if query_number == 0:
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_211_SIGNUP_SUCCESSFUL)
            else:
                return Response(serializers.errors, status=status.HTTP_220_DATA_NOT_VALID)
        else:
            return Response(serializers.errors, status=status.HTTP_210_ACCOUNT_EXIST)

    # Create your views here.
