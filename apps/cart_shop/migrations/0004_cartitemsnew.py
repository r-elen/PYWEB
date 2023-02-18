# Generated by Django 4.1.5 on 2023-02-18 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart_shop', '0003_cartuser_singleproduct_wishlist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemsNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart_shop.cartuser')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart_shop.singleproduct')),
            ],
        ),
    ]
