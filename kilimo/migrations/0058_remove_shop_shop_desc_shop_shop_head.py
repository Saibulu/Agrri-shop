# Generated by Django 5.0.7 on 2024-12-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0057_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='shop_desc',
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_head',
            field=models.CharField(default='Default Head', max_length=100),
        ),
    ]
