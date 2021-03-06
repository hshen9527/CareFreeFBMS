# Generated by Django 2.0.7 on 2018-09-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TraverMsg', '0004_auto_20180914_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenicmsg',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='scenicmsg',
            name='basic_desc',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='基本描述'),
        ),
        migrations.AddField(
            model_name='scenicmsg',
            name='link_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='景点链接'),
        ),
        migrations.AddField(
            model_name='scenicmsg',
            name='popular_level',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='受欢迎程度'),
        ),
    ]
