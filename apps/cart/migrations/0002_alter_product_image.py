# Generated by Django 4.1.5 on 2023-02-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/products/', null=True, upload_to='static/products/'),
        ),
    ]
