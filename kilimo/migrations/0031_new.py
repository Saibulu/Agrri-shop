# Generated by Django 5.1.3 on 2024-12-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0030_delete_blog"),
    ]

    operations = [
        migrations.CreateModel(
            name="New",
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
                ("new_head", models.CharField(max_length=100)),
                ("new_desc", models.TextField()),
            ],
        ),
    ]