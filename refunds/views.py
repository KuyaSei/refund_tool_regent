from django.shortcuts import render, redirect, get_object_or_404
from .models import RefundRequest
from .forms import RefundRequestForm, RefundStatusUpdateForm

# Create your views here.
def request_list(request):
    status_filter = request.GET.get("status")
    requests = RefundRequest.objects.all()

    if status_filter:
        requests = requests.filter(status=status_filter)

    context = {
        "requests": requests,
        "status_choices": RefundRequest.Status.choices,
        "selected_status": status_filter,
    }

    return render(request, "refunds/request_list.html", context)

def request_create(request):
    if request.method == "POST":
        form = RefundRequestForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect so that form will not be resubmitted during refresh
            return redirect("refunds:request_list")
    else:
        form = RefundRequestForm()

    return render(request, "refunds/request_form.html", {"form": form})

def request_update_status(request, pk):
    # return 404 if not found the specific refund request
    refund_request = get_object_or_404(RefundRequest, pk=pk)

    if request.method == "POST":
        form = RefundStatusUpdateForm(request.POST,
        instance=refund_request)
        if form.is_valid():
            form.save()
            return redirect("refunds:request_list")

    else:
        form = RefundStatusUpdateForm(instance=refund_request)

    return render(request, "refunds/request_update.html", {"form": form, "refund_request": refund_request,
    })
