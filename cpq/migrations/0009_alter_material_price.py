# Generated by Django 4.2.5 on 2023-10-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpq', '0008_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
