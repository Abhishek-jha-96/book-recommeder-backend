# In your users/serializers.py file
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    serializer for Custom User
    """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "bio", "birth_date", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=password,
            bio=validated_data.get("bio", ""),
            birth_date=validated_data.get("birth_date"),
        )
        return user
