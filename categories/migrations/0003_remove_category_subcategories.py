# Generated by Django 2.2.19 on 2021-04-03 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210403_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategories',
        ),
    ]
