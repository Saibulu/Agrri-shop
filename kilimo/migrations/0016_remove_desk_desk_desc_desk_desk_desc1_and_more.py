# Generated by Django 5.0.7 on 2024-11-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo', '0015_rename_desk_title_desk_desk_title1_desk_desk_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desk',
            name='desk_desc',
        ),
        migrations.AddField(
            model_name='desk',
            name='desk_desc1',
            field=models.TextField(default='Default description for desc1'),
        ),
        migrations.AddField(
            model_name='desk',
            name='desk_desc2',
            field=models.TextField(default='Default description for desc2'),
        ),
        migrations.AlterField(
            model_name='desk',
            name='desk_head',
            field=models.CharField(default='Default Head', max_length=100),
        ),
        migrations.AlterField(
            model_name='desk',
            name='desk_title1',
            field=models.CharField(default='Default Title 1', max_length=100),
        ),
        migrations.AlterField(
            model_name='desk',
            name='desk_title2',
            field=models.CharField(default='Default Title 2', max_length=100),
        ),
    ]