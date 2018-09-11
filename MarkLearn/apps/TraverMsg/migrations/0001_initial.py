# Generated by Django 2.0.7 on 2018-09-08 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMsg',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='城市id')),
                ('name', models.CharField(max_length=50, verbose_name='城市名称')),
                ('city_content', models.CharField(max_length=500, verbose_name='城市简介')),
                ('img_url', models.CharField(max_length=100, verbose_name='首页图片url')),
                ('province', models.CharField(max_length=20, verbose_name='所属省份')),
            ],
            options={
                'verbose_name': '城市信息',
                'verbose_name_plural': '城市信息',
            },
        ),
        migrations.CreateModel(
            name='ScenicMsg',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='景点id')),
                ('name', models.CharField(max_length=20, verbose_name='景点名称')),
                ('scenic_content', models.CharField(max_length=500, verbose_name='景点简介')),
                ('img_url', models.CharField(max_length=100, verbose_name='首页图片url')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TraverMsg.CityMsg', verbose_name='所属城市')),
            ],
            options={
                'verbose_name': '景点信息',
                'verbose_name_plural': '景点信息',
            },
        ),
        migrations.CreateModel(
            name='TraverMsg',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='行程id')),
                ('name', models.CharField(max_length=20, verbose_name='行程名称')),
                ('start_city', models.CharField(max_length=20, verbose_name='开始城市')),
                ('end_city', models.CharField(max_length=20, verbose_name='结束城市')),
                ('traverdays', models.CharField(max_length=3, verbose_name='行程天数')),
                ('adult_num', models.CharField(max_length=3, verbose_name='成人数量')),
                ('child_num', models.CharField(max_length=3, verbose_name='儿童数量')),
                ('traver_type', models.CharField(choices=[('single', '自驾游'), ('together', '跟团游')], default='single', max_length=10, verbose_name='旅游类型')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '行程信息',
                'verbose_name_plural': '行程信息',
            },
        ),
    ]