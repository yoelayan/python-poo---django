from django import forms
from .models import BankAccount


class BankAccount(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['number']
