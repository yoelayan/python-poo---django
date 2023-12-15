
from django.urls import path
from .views import BankAccountsListView, BankAccountCreateView


urlpatterns = [
    path("", BankAccountsListView.as_view(), name="list_accounts"),
    path("create", BankAccountCreateView.as_view(), name="create_account")
]
