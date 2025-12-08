from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Prompt, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )
        return user


class PromptSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)

    class Meta:
        model = Prompt
        fields = "__all__"
        read_only_fields = ["seller", "created_at"]


class OrderSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    prompt = PromptSerializer(read_only=True)
    prompt_id = serializers.PrimaryKeyRelatedField(
        source="prompt", queryset=Prompt.objects.all(), write_only=True
    )

    class Meta:
        model = Order
        fields = ["id", "buyer", "prompt", "prompt_id", "status", "amount", "created_at", "payment_id"]
        read_only_fields = ["buyer", "status", "created_at", "payment_id"]
