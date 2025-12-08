from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from store.views import RegisterView, PromptViewSet, OrderViewSet

router = DefaultRouter()
router.register("prompts", PromptViewSet, basename="prompt")
router.register("orders", OrderViewSet, basename="order")

from django.http import JsonResponse

def index(request):
    return JsonResponse({"status": "running", "msg": "PromptStore API working!"})

urlpatterns = [
    path("", index),  # <- add this line
    path("admin/", admin.site.urls),
    path("api/auth/register/", RegisterView.as_view()),
    path("api/auth/token/", TokenObtainPairView.as_view()),
    path("api/auth/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
]
