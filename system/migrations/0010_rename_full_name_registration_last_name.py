# Generated by Django 5.0.7 on 2024-09-02 01:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0009_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="registration",
            old_name="full_name",
            new_name="last_name",
        ),
    ]
