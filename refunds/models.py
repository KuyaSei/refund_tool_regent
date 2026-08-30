from django.db import models

class RefundRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"
        REFUNDED = "REFUNDED", "Refunded"


    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2) # decimal and not float as money is involved here
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING, # every new request starts with pending first as its default status
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.refund_amount} - ({self.status})"

    class Meta:
        ordering = ["-created_at"] #newest requests will be shown first in the list 