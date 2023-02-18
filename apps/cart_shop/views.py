from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import Wishlist, CartItemsNew


class ViewCart(View):
   def get(self, request):

        data = CartItemsNew.objects.all()
        context = {'data': data}
        return render(request, 'cart_shop/cart.html', context)


class ViewWishlist(View):
   def get(self, request):
       data = Wishlist.objects.all()
       context = {'data': data}

       return render(request, 'cart_shop/wishlist.html', context)

