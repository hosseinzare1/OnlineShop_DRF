from django.shortcuts import render
from django.views.static import serve
from rest_framework.views import APIView
from rest_framework.response import Response
from users_api import status
from users_api.serializer import UserModelSerializers
from users_api.models import User


class Login(APIView):
    def post(self, request):
        serializers = UserModelSerializers(data=request.data)
        #
        number = serializers.initial_data.get('number')
        password = serializers.initial_data.get('password')

        # return Response(serializers.data, status=status.HTTP_3000_INCORRECT)

        if serializers.is_valid():
            query_number = User.objects.filter(number=number).count()
            if query_number > 0:
                query_number_password = User.objects.filter(number=number, password=password).count()
                if query_number_password > 0:
                    # serializers.save()
                    return Response(serializers.data, status=status.HTTP_212_LOGIN_SUCCESSFUL)
                else:
                    return Response(serializers.data, status=status.HTTP_214_PASSWORD_WRONG)
            else:
                return Response(serializers.data, status=status.HTTP_213_THERE_IS_NO_ACCOUNT)
        else:
            return Response(serializers.errors, status=status.HTTP_220_DATA_NOT_VALID)


class Signup(APIView):
    def post(self, request):
        serializers = UserModelSerializers(data=request.data)

        name = serializers.initial_data.get('name')
        number = serializers.initial_data.get('number')
        password = serializers.initial_data.get('password')

        query_number = User.objects.filter(number=number).count()

        if serializers.is_valid():
            if query_number == 0:
                serializers.save()
                return Response(serializers.data, status=status.HTTP_211_SIGNUP_SUCCESSFUL)
            else:
                return Response(serializers.errors, status=status.HTTP_210_ACCOUNT_EXIST)
        else:
            return Response(serializers.errors, status=status.HTTP_220_DATA_NOT_VALID)
# Create your views here.
