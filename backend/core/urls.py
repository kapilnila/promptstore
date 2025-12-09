from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from store.views import RegisterView, PromptViewSet, OrderViewSet
from django.http import JsonResponse

router = DefaultRouter()
router.register("prompts", PromptViewSet, basename="prompts")
router.register("orders", OrderViewSet, basename="orders")

def index(request):
    return JsonResponse({"status": "running", "msg": "Prompt Store Backend Live"})

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),

    # AUTH
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="refresh"),

    # API router
    path("api/", include(router.urls)),
]
