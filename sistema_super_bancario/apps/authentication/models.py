import hashlib

from django.contrib.auth.models import AbstractUser
from django.db import models


class BankUser(AbstractUser):
    identification_number = models.CharField(max_length=30)
    secret_key = models.CharField(max_length=250, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="bankuser_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="bankuser_set",
        related_query_name="user",
    )

    def save(self, *args, **kwargs):
        try:
            self.secret_key = hashlib.sha256(
                self.secret_key.encode()).hexdigest()
        except AttributeError:
            self.secret_key = ''
        super().save(*args, **kwargs)

    def validate_secret_key(self, secret_key: str):
        return self.secret_key == hashlib.sha256(
            secret_key.encode()).hexdigest()

    class Meta:
        verbose_name = "Usuario"