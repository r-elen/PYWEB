# Generated by Django 4.1.5 on 2023-02-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_shop', '0005_alter_singleproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/products/'),
        ),
    ]
