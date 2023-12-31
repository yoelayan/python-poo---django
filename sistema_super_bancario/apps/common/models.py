from django.db import models


class CommonKind(models.Model):
    description = models.CharField(max_length=250)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.description

    class Meta:
        abstract = True
