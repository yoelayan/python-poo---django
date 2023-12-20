from django.contrib import admin
from .models import (
    Currency,
    KindRequestAperture,
    KindTransaction,
    BankAccount,
    Transaction,
    BankRequestAperture,
)


models = [
    Currency,
    KindRequestAperture,
    KindTransaction,
    BankAccount,
    Transaction,
    BankRequestAperture,
]

for model in models:
    admin.site.register(model)
