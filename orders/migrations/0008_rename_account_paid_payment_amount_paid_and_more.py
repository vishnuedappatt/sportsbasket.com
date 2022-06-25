# Generated by Django 4.0.4 on 2022-06-10 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_payment_order_id_payment_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='account_paid',
            new_name='amount_paid',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]
