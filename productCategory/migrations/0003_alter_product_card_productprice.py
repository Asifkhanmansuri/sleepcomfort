# Generated by Django 4.1.7 on 2023-06-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productCategory', '0002_product_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_card',
            name='Productprice',
            field=models.CharField(max_length=50),
        ),
    ]
