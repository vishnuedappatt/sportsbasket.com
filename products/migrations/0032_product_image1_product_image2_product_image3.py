# Generated by Django 4.0.4 on 2022-06-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
