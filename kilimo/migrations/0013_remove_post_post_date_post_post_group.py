# Generated by Django 5.0.7 on 2024-11-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0012_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
        migrations.AddField(
            model_name='post',
            name='post_group',
            field=models.TextField(default='default_group'),
        ),
    ]
