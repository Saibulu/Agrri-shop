# Generated by Django 5.0.7 on 2024-12-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kilimo", "0082_remove_pixel_month"),
    ]

    operations = [
        migrations.AddField(
            model_name="pixel",
            name="date",
            field=models.DateField(default="2024-07-08"),
        ),
        migrations.AddField(
            model_name="pixel",
            name="month",
            field=models.CharField(default="none", max_length=100),
        ),
    ]
