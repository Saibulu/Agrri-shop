# Generated by Django 5.1.3 on 2024-12-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0034_remove_section_section_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                (
                    "image_img",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]
