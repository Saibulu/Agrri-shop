# Generated by Django 5.0.7 on 2024-12-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0074_pixel_redeem_date_pixel_redeem_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixel',
            name='redeem_date',
            field=models.IntegerField(default='2024-07-08'),
        ),
    ]
