from rest_framework import serializers
from .models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    test_data = serializers.CharField(max_length=2000)

    class Meta:
        model = UserData
        fields = ('__all__')
