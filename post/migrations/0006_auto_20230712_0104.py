# Generated by Django 3.2.20 on 2023-07-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
