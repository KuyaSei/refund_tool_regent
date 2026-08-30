from django import forms
from .models import RefundRequest

class RefundRequestForm(forms.ModelForm):
    class Meta:
        model = RefundRequest
        fields = ["customer_name", "customer_email", "refund_amount", "reason"]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_email": forms.EmailInput(attrs={"class": "form-control"}),
            "refund_amount": forms.NumberInput(attrs={"class": "form-control"}),
            "reason": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def clean_refund_amount(self):
        # 0 or negative refund amount is not allowed
        amount = self.cleaned_data.get("refund_amount")
        if amount is not None and amount <= 0:
            raise forms.ValidationError("Refund amount must be greater than zero.")
        return amount

class RefundStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = RefundRequest
        # We will only allow updating the status field
        fields = ["status"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
        }