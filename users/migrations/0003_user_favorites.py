# Generated by Django 2.2.19 on 2021-04-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210403_0503'),
        ('users', '0002_auto_20210328_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]