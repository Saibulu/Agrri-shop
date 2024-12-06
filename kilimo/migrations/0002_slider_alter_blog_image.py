# Generated by Django 5.0.7 on 2024-11-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slider_head', models.CharField(max_length=50)),
                ('Slider_desc', models.TextField()),
                ('Slider_image', models.ImageField(upload_to='Sliders/')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs/'),
        ),
    ]
