# Generated by Django 2.0.7 on 2018-09-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0006_auto_20180914_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelmsg',
            name='scenic_name',
        ),
        migrations.AlterField(
            model_name='hotelmsg',
            name='hotel_content',
            field=models.CharField(max_length=300, verbose_name='酒店位置'),
        ),
    ]
