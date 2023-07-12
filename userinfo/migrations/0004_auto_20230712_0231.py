# Generated by Django 3.2.20 on 2023-07-11 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20230712_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='feature',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='blood',
            field=models.CharField(choices=[('미기재', 'Undefined'), ('A (RH+)', 'A Positive'), ('B (RH+)', 'B Positive'), ('O (RH+)', 'O Positive'), ('AB (RH+)', 'Ab Positive'), ('A (RH-)', 'A Negative'), ('B (RH-)', 'B Negative'), ('O (RH-)', 'O Negative'), ('AB (RH-)', 'Ab Negative')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hair',
            field=models.CharField(choices=[('미기재', 'Undefined'), ('삭발', 'Shaved'), ('대머리', 'Bald'), ('긴머리', 'Long Hair'), ('곱슬긴머리', 'Curly Long Hair'), ('단발머리', 'Short Hair'), ('커트머리', 'Cut Hair'), ('곱슬단발머리', 'Curly Short Hair'), ('가발', 'Wig'), ('스포츠형', 'Sporty'), ('짧은머리(생머리)', 'Short Natural Hair'), ('긴머리(생머리)', 'Long Natural Hair'), ('짧은머리(펌)', 'Short Permed Hair'), ('긴머리(펌)', 'Long Permed Hair'), ('묶음머리', 'Tied Hair'), ('상고머리', 'Topknot'), ('염색/탈색', 'Dyed Bleached'), ('바가지머리', 'Bowl Cut'), ('기타', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='scar',
            field=models.CharField(choices=[('미기재', 'Undefined'), ('머리', 'Head'), ('얼굴', 'Face'), ('팔', 'Arm'), ('손', 'Hand'), ('등', 'Back'), ('몸통', 'Torso'), ('둔부', 'Buttock'), ('다리', 'Leg'), ('발', 'Foot'), ('기타', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tooth',
            field=models.CharField(choices=[('정상', 'Normal'), ('틀니', 'Denture'), ('뻐드렁니', 'Wisdom Tooth'), ('금니', 'Molar'), ('은니', 'Silver Tooth'), ('의치', 'Dental Bridge'), ('때운이빨', 'Tartar Tooth'), ('임플란트', 'Implant'), ('기타', 'Other')], max_length=100),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('userimg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userinfo.userinfo')),
            ],
        ),
    ]