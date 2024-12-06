# Generated by Django 5.0.7 on 2024-11-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0009_remove_details_detail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(max_length=100)),
                ('case_image', models.ImageField(blank=True, null=True, upload_to='cases/')),
                ('case_desc', models.TextField()),
            ],
        ),
    ]
