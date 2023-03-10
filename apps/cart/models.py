from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.user}"


class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   description = models.TextField()
   image = models.ImageField(upload_to='static/products/', null=True, blank=True, default='static/products/')
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.name}, {self.price}"


class CartItem(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.cart}_{self.product}"