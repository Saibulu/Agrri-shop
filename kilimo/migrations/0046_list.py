# Generated by Django 5.0.7 on 2024-12-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0045_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=100)),
                ('list_desc', models.TextField()),
            ],
        ),
    ]
