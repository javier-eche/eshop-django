# Generated by Django 2.2.19 on 2021-04-03 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item_order', '0002_auto_20210403_0647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['product']},
        ),
    ]