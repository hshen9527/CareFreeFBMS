# Generated by Django 2.0.7 on 2018-09-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0013_auto_20180911_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsmsg',
            name='city_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='所属城市'),
        ),
    ]
