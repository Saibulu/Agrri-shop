# Generated by Django 5.0.7 on 2024-12-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0063_alx"),
    ]

    operations = [
        migrations.CreateModel(
            name="Redeem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("redeem_title", models.CharField(max_length=100)),
                ("redeem_head", models.CharField(max_length=100)),
            ],
        ),
    ]