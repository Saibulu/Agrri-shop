# Generated by Django 5.0.7 on 2024-12-07 19:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0069_tax"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tax",
        ),
    ]