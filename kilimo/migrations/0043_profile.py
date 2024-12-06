# Generated by Django 5.0.7 on 2024-12-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0042_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_title', models.CharField(max_length=100)),
                ('profile_desc', models.TextField()),
                ('profile_image', models.ImageField(default='default_image.jpg', upload_to='profiles/')),
                ('profile_number', models.IntegerField()),
            ],
        ),
    ]