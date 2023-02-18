from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartUser, SingleProduct, Wishlist

admin.site.register(CartUser)
admin.site.register(SingleProduct)
admin.site.register(Wishlist)

