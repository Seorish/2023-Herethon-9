# Generated by Django 3.2.20 on 2023-07-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('resiNumStart', models.PositiveIntegerField()),
                ('resiNumEnd', models.PositiveIntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('tooth', models.CharField(choices=[('정상', '정상'), ('틀니', '틀니'), ('뻐드렁니', '뻐드렁니'), ('옹니', '옹니'), ('금니', '금니'), ('은니', '은니'), ('의치', '의치'), ('때운이빨', '때운이빨'), ('임플란트', '임플란트'), ('기타', '기타')], max_length=100)),
            ],
        ),
    ]