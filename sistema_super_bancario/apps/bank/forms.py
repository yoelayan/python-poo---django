from django import forms


class DepositAndWithdrawForm(forms.Form):
    amount = forms.DecimalField(label="Monto")
    secret_key = forms.CharField(label="Clave Secreta")
