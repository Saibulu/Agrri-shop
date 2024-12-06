# Generated by Django 5.0.7 on 2024-12-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0028_moon'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=100)),
                ('about_head', models.CharField(max_length=100)),
                ('about_desc', models.TextField()),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='about/')),
            ],
        ),
    ]