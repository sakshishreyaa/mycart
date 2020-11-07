# Generated by Django 3.1.2 on 2020-11-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200607_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
