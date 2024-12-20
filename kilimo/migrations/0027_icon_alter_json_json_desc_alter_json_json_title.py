# Generated by Django 5.0.7 on 2024-11-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0026_remove_json_json_image_json_json_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_title', models.CharField(max_length=100)),
                ('icon_desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='json',
            name='json_desc',
            field=models.TextField(default='text.'),
        ),
        migrations.AlterField(
            model_name='json',
            name='json_title',
            field=models.CharField(default='image', max_length=100),
        ),
    ]
