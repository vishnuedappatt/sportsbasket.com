# Generated by Django 4.0.4 on 2022-06-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_product_image1_product_image2_product_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcoupon',
            name='active_from',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
