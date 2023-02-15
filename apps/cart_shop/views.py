from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


class ViewCart(View):
   def get(self, request):
       return render(request, 'cart_shop/cart.html')

class ViewWishlist(View):
   def get(self, request):
       context = {'data': [
                            {'name': 'Bell Pepper',
                            'price': 4.90,
                            'total_price': 4.90,
                            'url': 'shop/images/product-1.jpg'},

                            {'name': 'Strawberry',
                            'price': 15.70,
                            'total_price': 15.70,
                            'url': 'shop/images/product-2.jpg'},

                            {'name': 'Green Beans',
                            'price': 25.90,
                            'total_price': 25.90,
                            'url': 'shop/images/product-3.jpg'},

                            {'name': 'Purple Cabbage',
                            'price': 7.50,
                            'total_price': 7.50,
                            'url': 'shop/images/product-4.jpg'},

                            {'name': 'Tomatoe',
                            'price': 12.40,
                            'total_price': 12.40,
                            'url': 'shop/images/product-5.jpg'},

                           ]
                  }

       return render(request, 'cart_shop/wishlist.html', context)

