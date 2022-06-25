# Generated by Django 4.0.4 on 2022-06-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_rename_account_paid_payment_amount_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Failure', 'Failure')], default='New', max_length=10),
        ),
    ]
