# Generated by Django 3.2.20 on 2023-07-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_auto_20230712_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]