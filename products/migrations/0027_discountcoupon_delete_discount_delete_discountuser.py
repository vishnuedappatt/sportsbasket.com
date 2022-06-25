# Generated by Django 4.0.4 on 2022-06-14 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_remove_discountuser_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=10)),
                ('discount', models.DecimalField(decimal_places=3, max_digits=5)),
                ('active_from', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='DiscountUser',
        ),
    ]
