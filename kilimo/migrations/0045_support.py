# Generated by Django 5.0.7 on 2024-12-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0044_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support_title', models.CharField(max_length=100)),
                ('support_desc', models.TextField()),
            ],
        ),
    ]
