from django.db import models
from django.db import models

# Bidhaa
class Item(models.Model):
    name = models.CharField(max_length=100)         # jina la bidhaa
    price = models.DecimalField(max_digits=10, decimal_places=2)  # bei

    def __str__(self):
        return f"{self.name} - {self.price} TZS"
# Order ya mteja
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    customer_phone = models.CharField(max_length=15)      # namba ya simu
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # bidhaa iliyochaguliwa
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # kiasi cha malipo
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # hali ya order
    created_at = models.DateTimeField(auto_now_add=True)  # tarehe ya kuunda

    def __str__(self):
        return f"Order {self.id} - {self.item.name} ({self.status})"
