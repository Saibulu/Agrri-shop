# Generated by Django 5.0.7 on 2024-12-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0062_special"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alx",
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
                ("alx_title", models.CharField(max_length=100)),
                ("alx_head", models.CharField(max_length=100)),
            ],
        ),
    ]
