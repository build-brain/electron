from rest_framework import serializers
from django.conf import settings
from management.models import *


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer.

    Used in POST and GET
    """

    password1 = serializers.CharField(
        write_only=True,
        min_length=settings.MIN_PASSWORD_LENGTH,
        error_messages={
            "min_length": "Password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        },
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=settings.MIN_PASSWORD_LENGTH,
        error_messages={
            "min_length": "Password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        },
    )

    class Meta:
        model = User
        fields = ("id", "phone_number", "first_name", "last_name", "password1", "password2")
        read_only_fields = ("id",)

    def validate(self, data):
        """
        Validates if both password are same or not.
        """

        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Пароли не совпадают!")
        return data

    def create(self, validated_data):
        user = User(phone_number=validated_data["phone_number"])
        user.set_password(validated_data["password1"])
        user.save()
        return user


class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = "__all__"
