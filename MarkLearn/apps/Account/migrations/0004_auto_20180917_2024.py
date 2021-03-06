# Generated by Django 2.0.7 on 2018-09-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20180917_0117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signon',
            options={'verbose_name': '登陆表', 'verbose_name_plural': '登陆表'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=10, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='畅游网用户', max_length=50, verbose_name='昵称'),
        ),
    ]
