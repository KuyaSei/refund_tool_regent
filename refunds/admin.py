from django.contrib import admin
from .models import RefundRequest

# Register your models here.
@admin.register(RefundRequest)
class RefundRequestAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_email", "refund_amount", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("customer_name", "customer_email", "reason")

