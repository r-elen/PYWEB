# Generated by Django 4.1.5 on 2023-02-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/products/', null=True, upload_to='static/products/'),
        ),
    ]
