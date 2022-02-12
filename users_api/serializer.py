from rest_framework.serializers import ModelSerializer
from users_api import models


class UserModelSerializers(ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"
