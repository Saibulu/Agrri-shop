# Generated by Django 5.0.7 on 2024-11-28 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0008_details_detail_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='detail_image',
        ),
    ]
