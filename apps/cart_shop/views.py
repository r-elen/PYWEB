from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import CartUser, SingleProduct, Wishlist


class ViewCart(View):
   def get(self, request):
       return render(request, 'cart_shop/cart.html')

class ViewWishlist(View):
   def get(self, request):
       data = Wishlist.objects.all()
       context = {'data': data}

       return render(request, 'cart_shop/wishlist.html', context)

