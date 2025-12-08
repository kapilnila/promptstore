from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Prompt, Order
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    PromptSerializer,
    OrderSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all().order_by("-created_at")
    serializer_class = PromptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        # In real life you'd integrate Stripe/Razorpay here
        prompt = serializer.validated_data["prompt"]
        serializer.save(buyer=self.request.user, amount=prompt.price, status="PAID")
