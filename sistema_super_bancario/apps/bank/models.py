import random
import string

from django.db import models
from apps.common.models import CommonKind
from apps.authentication.models import BankUser

from decimal import Decimal
from django.core.mail import send_mail

from django.core.exceptions import ValidationError


class Currency(CommonKind):
    pass


class KindRequestAperture(CommonKind):
    pass


class KindTransaction(CommonKind):
    pass


class BankAccount(models.Model):
    user = models.ForeignKey(BankUser, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        verbose_name='Saldo'
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.DO_NOTHING,
        null=True
    )
    linked_accounts = models.ManyToManyField(
        'self', blank=True
    )
    token = models.CharField(
        max_length=64, default='', editable=False
    )

    def __str__(self):
        return f'{self.account_number} - {self.currency.description} - {self.user.get_full_name()}'

    def generate_token(self):
        self.token = ''.join(
            random.choices(string.ascii_letters + string.digits, k=64)
        )
        self.save()
        return self.token

    def valid_token(self, token):
        if not token or token != self.token:
            print(token, self.token)
            raise ValidationError("El token proporcionado no es valido.")
        self.generate_token()

    def add_transaction(self, code: str, amount: float):
        try:
            Transaction.objects.create(
                bank_account=self,
                kind=KindTransaction.objects.get(code=code),
                amount=amount
            )
        except KindTransaction.DoesNotExist:
            raise ValidationError("El codigo de la transaccion no existe.")

    def deposit(self, amount: Decimal, token: str = None):
        self.valid_token(token)
        self.balance += amount
        self.save()
        self.add_transaction('DEP', amount)

    def send(
        self, amount: Decimal,
        destiny_account: 'BankAccount',
        token: str = None
    ):
        self.valid_token(token)
        self.balance -= amount
        destiny_account.balance += amount
        destiny_account.save()
        destiny_account.add_transaction('DEP', amount)
        self.save()
        self.add_transaction('SEND', amount)

    def withdraw(self, amount: Decimal, token: str = None):
        self.valid_token(token)
        self.balance -= amount
        self.save()
        self.add_transaction('OUT', amount)

    @staticmethod
    def get_conf_table(queryset=None):
        if not queryset:
            queryset = BankAccount.objects.all()
        return {
            'title': 'Cuentas Bancarias',
            'header': [
                {
                    'name': 'Numero de cuenta',
                    'item': 'number',
                    'type': 'text'
                },
                {
                    'name': 'Monto Actual',
                    'item': 'actual_amount',
                    'type': 'text'
                },
                {
                    'name': 'Monto Actual x2',
                    'item': 'actual_amount_interest',
                    'type': 'text'
                },
            ],
            'prefix': 'bank_ac',
            'data': queryset
        }


class Transaction(models.Model):

    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE,
        related_name="transactions"
    )
    kind = models.ForeignKey(
        KindTransaction, on_delete=models.DO_NOTHING,
        null=True
    )
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        verbose_name='Monto'
    )
    create_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return f'{self.kind} - {self.amount} : {self.create_at}'


class BankRequestAperture(models.Model):
    client_name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.EmailField(max_length=260)
    city = models.CharField(max_length=250, verbose_name="Ciudad")
    details = models.TextField(verbose_name="Detalles de la solicitud")
    kind = models.ForeignKey(
        KindRequestAperture, null=True, on_delete=models.DO_NOTHING,
        verbose_name="Tipo de solicitud"
    )
    is_approved = models.BooleanField(default=None, null=True)

    def __str__(self):
        return f'{self.client_name} - {self.email} - {self.city}'

    def send_approval_email(self):
        if self.is_approved:
            print("Mensaje Enviado!")
            """
            send_mail(
                'Aprobacion',
                'Solicitud aprobada!',
                "formativa@example.com",
                [self.email]
            )
            """
