# Generated by Django 5.0.7 on 2024-11-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0021_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_title', models.CharField(max_length=100)),
                ('testimonial_desc', models.TextField()),
            ],
        ),
    ]