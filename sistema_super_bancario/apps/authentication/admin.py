from django.contrib import admin
from apps.authentication.models import BankUser


models = [
    BankUser
]

for model in models:
    admin.site.register(model)
