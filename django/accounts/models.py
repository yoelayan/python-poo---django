from django.db import models


class Account(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
