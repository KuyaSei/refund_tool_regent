from django.urls import path
from .import views

app_name = "refunds"

urlpatterns = [
    path("", views.request_list, name="request_list"),
    path("create/", views.request_create, name="request_create"),
    path("<int:pk>/update/>", views.request_update_status, name="request_update_status")
]