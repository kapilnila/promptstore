
from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prompts")
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()  # actual prompt text
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.CharField(max_length=255, blank=True)  # comma separated
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("FAILED", "Failed"),
    )
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.buyer.username} -> {self.prompt.title} ({self.status})"
