# Generated by Django 2.0.7 on 2018-09-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0002_auto_20180913_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmsg',
            name='product_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='产品类型'),
        ),
    ]
