# Generated by Django 5.0.7 on 2024-12-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0064_redeem'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_title', models.CharField(max_length=100)),
                ('user_head', models.CharField(max_length=100)),
            ],
        ),
    ]