# Generated by Django 2.2.19 on 2021-04-03 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
