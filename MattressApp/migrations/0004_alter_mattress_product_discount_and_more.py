# Generated by Django 4.1.7 on 2023-06-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MattressApp', '0003_alter_mattress_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mattress_product',
            name='Discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mattress_product',
            name='Product_Price',
            field=models.IntegerField(),
        ),
    ]
