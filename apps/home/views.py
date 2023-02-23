from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import SingleProduct
from apps.cart_shop.views import fill_card_in_session, fill_id_card_in_session


class IndexShopView(View):
   def get(self, request):
       fill_card_in_session(request)
       fill_id_card_in_session(request)

       data = SingleProduct.objects.all()
       context = {'data': data}
       return render(request, 'home/index.html', context)

class ViewAboout(View):
   def get(self, request):
       return render(request, 'home/about.html')

class ViewContact(View):
   def get(self, request):
       return render(request, 'home/contact.html')

class ViewWishlist(View):
   def get(self, request):
       return render(request, 'home/wishlist.html')



