# Generated by Django 5.0.7 on 2024-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0004_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("LIPA KWA SIMU", "LIPA KWA SIMU"),
                    ("TIGO PESA", "TIGO PESA"),
                    ("AIRTEL MONEY", "AIRTEL MONEY"),
                    ("NMB", "NMB"),
                ],
                max_length=255,
            ),
        ),
    ]
