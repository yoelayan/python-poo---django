from django.shortcuts import render

from .models import Account


def ver_cuentas(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'index.html', context)
