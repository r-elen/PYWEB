from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartItemShop, Product

admin.site.register(CartItemShop)
admin.site.register(Product)
