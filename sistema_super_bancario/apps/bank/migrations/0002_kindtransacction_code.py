# Generated by Django 5.0 on 2023-12-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bank", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="kindtransacction",
            name="code",
            field=models.CharField(default="N/A", max_length=10),
        ),
    ]
