from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.exceptions import ValidationError
from django.views.generic import View

from apps.bank.models import BankAccount
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BankRequestAperture
from .forms import DepositAndWithdrawForm
from decimal import Decimal


class MainView(View):
    template_name = 'main.html'

    def get(self, request):

        return render(request, self.template_name)


class SuccessRequestAppertureView(View):
    template_name = 'bank/success_request_apperture.html'

    def get(self, request):

        return render(request, self.template_name)


class DashboardView(View, LoginRequiredMixin):
    template_name = 'bank/dashboard.html'

    def get(self, request):
        accounts = BankAccount.objects.filter(user=request.user)

        context = {
            "accounts": accounts
        }
        return render(request, self.template_name, context)


class RequestAppertureView(CreateView):
    template_name = 'form.html'
    model = BankRequestAperture
    fields = ['client_name', 'email', 'kind', 'city', 'details']
    success_url = reverse_lazy("success_request_apperture")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Solicitud de Apertura de cuenta'
        return context


class BankAccountsListView(ListView):
    model = BankAccount
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['table'] = BankAccount.get_conf_table()
        return context


class BankAccountCreateView(CreateView):
    model = BankAccount
    fields = ['number', 'actual_amount']
    template_name = 'form.html'
    success_url = reverse_lazy('list_accounts')


class DepositView(View, LoginRequiredMixin):
    template_name = 'form.html'

    def post(self, request, pk=None):
        amount = request.POST.get("amount", None)
        secret_key = request.POST.get("secret_key", None)
        form = DepositAndWithdrawForm()
        try:
            account = BankAccount.objects.get(pk=pk)
        except BankAccount.DoesNotExist:
            raise ValidationError("La cuenta no existe")

        user = request.user
        is_valid = user.validate_secret_key(secret_key)
        if is_valid:
            token = account.generate_token()
            account.deposit(Decimal(amount), token)
        else:
            raise ValidationError("Clave Incorrecta")
        context = {
            "title": f"Depositar para la cuenta de: {account.user.get_full_name()}",
            "object": account,
            "form": form
        }
        return render(request, self.template_name, context)

    def get(self, request, pk=None):
        try:
            account = BankAccount.objects.get(pk=pk)
        except BankAccount.DoesNotExist:
            raise ValidationError("La cuenta no existe")
        form = DepositAndWithdrawForm()

        context = {
            "title": f"Depositar para la cuenta de: {account.user.get_full_name()}",
            "object": account,
            "form": form
        }
        return render(request, self.template_name, context)
