from typing import Any
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from apps.bank.models import BankAccount
from django.urls import reverse_lazy


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
