# Generated by Django 5.1.3 on 2024-12-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0037_excel_delete_image_alter_about_about_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("cart_title", models.CharField(max_length=100)),
                ("cart_head", models.CharField(max_length=100)),
            ],
        ),
    ]