# Generated by Django 2.2.19 on 2021-04-03 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210403_0503'),
        ('item_order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='product',
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]
