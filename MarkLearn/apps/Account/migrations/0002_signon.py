# Generated by Django 2.0.7 on 2018-09-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signon',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
            ],
        ),
    ]
