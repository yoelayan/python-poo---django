
from django.urls import path
from .views import (
    BankAccountsListView, BankAccountCreateView, RequestAppertureView,
    SuccessRequestAppertureView, DashboardView, DepositView
)


urlpatterns = [
    path("", BankAccountsListView.as_view(), name="list_accounts"),
    path("create", BankAccountCreateView.as_view(), name="create_account"),
    path(
        "request_apperture",
        RequestAppertureView.as_view(), name="apperture_account"
    ),
    path(
        "success_request",
        SuccessRequestAppertureView.as_view(), name="success_request_apperture"
    ),
    path(
        "dashboard",
        DashboardView.as_view(), name="dashboard"
    ),
    path(
        "deposit/<int:pk>/",
        DepositView.as_view(), name="deposit"
    ),
]
