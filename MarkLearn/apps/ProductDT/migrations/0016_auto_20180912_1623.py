# Generated by Django 2.0.7 on 2018-09-12 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0015_auto_20180912_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.CharField(max_length=100, verbose_name='供应城市')),
                ('product_price', models.CharField(max_length=10, verbose_name='对应价格')),
            ],
            options={
                'verbose_name': '产品供应表',
                'verbose_name_plural': '产品供应表',
            },
        ),
        migrations.CreateModel(
            name='Product_Senic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senic_name', models.CharField(max_length=100, verbose_name='景点')),
            ],
            options={
                'verbose_name': '产品景点表',
                'verbose_name_plural': '产品景点表',
            },
        ),
        migrations.RemoveField(
            model_name='productmsg',
            name='product_price',
        ),
        migrations.RemoveField(
            model_name='productmsg',
            name='scenic_name',
        ),
        migrations.RemoveField(
            model_name='productmsg',
            name='start_city',
        ),
        migrations.AddField(
            model_name='product_senic',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductDT.ProductMsg', verbose_name='产品id'),
        ),
        migrations.AddField(
            model_name='product_city',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductDT.ProductMsg', verbose_name='产品id'),
        ),
        migrations.AlterUniqueTogether(
            name='product_city',
            unique_together={('product_id', 'city_id')},
        ),
    ]