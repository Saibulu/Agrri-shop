# Generated by Django 5.0.7 on 2024-11-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0027_icon_alter_json_json_desc_alter_json_json_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moon_title', models.CharField(max_length=100)),
                ('moon_head', models.CharField(max_length=100)),
            ],
        ),
    ]
