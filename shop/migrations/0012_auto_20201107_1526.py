# Generated by Django 3.1.2 on 2020-11-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('clothing', 'clothing'), ('accessories', 'accessories'), ('footwear', 'footwear')], max_length=50),
        ),
    ]
