from django.db import models


class BankAccount(models.Model):
    number = models.CharField(max_length=20)
    actual_amount = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        verbose_name='Saldo'
    )

    def __str__(self):
        return self.number

    @property
    def actual_amount_interest(self):
        return self.actual_amount * 2

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


class KindTransaction(models.Model):
    description = models.CharField(max_length=250)
    code = models.CharField(default="N/A", max_length=10)

    def __str__(self):
        return self.description


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
