from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from .models import Wishlist, CartItemsNew, SingleProduct, CartUser
from decimal import Decimal


def fill_card_in_session(request):
   cart = request.session.get('cart', {})
   if request.user.is_authenticated and not cart:
       if not cart:
           cart_items = CartItemsNew.objects.filter(cart__user=request.user)
           for item in cart_items:
               cart[item.product.id] = item.quantity
           request.session['cart'] = cart
       return cart


def fill_id_card_in_session(request):
   id_cart = request.session.get('id_cart', None)
   if request.user.is_authenticated and not id_cart:
       if not id_cart:
           id_cart = CartUser.objects.get(user=request.user).id
           request.session['id_cart'] = id_cart
       return id_cart


class ViewCart(View):
   def get(self, request):
       if request.user.is_authenticated:
            data = CartItemsNew.objects.filter(cart__user=request.user)
            context = {'data': data}

            # cart_items = CartItemsNew.objects.filter(cart__user=request.user)
            # total_price = sum(item.product.price * item.quantity for item in cart_items)

            total_price_no_discount = sum(item.product.price * item.quantity for item in data)
            if not total_price_no_discount:
                total_price_no_discount = Decimal("0.00")

            total_discount = sum(item.product.price * item.product.discount * item.quantity for item in data if item.product.discount is not None) / 100

            if not total_discount:
                total_discount = Decimal("0.00")
            total_sum = total_price_no_discount - total_discount
            context = {'data': data,
                       'total_price_no_discount': total_price_no_discount,
                       'total_discount': total_discount,
                       'total_price': total_sum,
                       }

            return render(request, 'cart_shop/cart.html', context)
       return render(request, 'cart_shop/cart.html')


class ViewCartBuy(View):
   def get(self, request, product_id):
       if request.user.is_authenticated:
           product = get_object_or_404(SingleProduct, id=product_id)
           cart_user = get_object_or_404(CartUser, user=request.user)
           cart_item = CartItemsNew(cart=cart_user, product=product)
           cart_item.save()
           return redirect('cart_shop:cart')

       return redirect('auth_shop:login')

class ViewCartDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemsNew, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')


class ViewCartAdd(View):
   def get(self, request, product_id):
       if request.user.is_authenticated:
           product = get_object_or_404(SingleProduct, id=product_id)
           cart_user = get_object_or_404(CartUser, user=request.user)
           cart_item = CartItemsNew(cart=cart_user, product=product)
           cart_item.save()
           return redirect('home:index')
       return redirect('auth_shop:login')


# def view_cart_total(request):
   # cart_items = CartItemsNew.objects.filter(cart__user=request.user)
   # total_price = sum(item.product.price * item.quantity for item in cart_items)
   # context = {'cart_items': cart_items, 'total_price': total_price}
   # return render(request, 'cart_shop/cart.html', context)

def update_item(request, item_id):
   item = CartItemsNew.objects.get(id=item_id)
   item.quantity += int(request.GET.get('quantity'))
   item.save()
   return redirect('cart_shop:cart')



def checkout_cart(request):
   # code to handle checkout process
   return redirect('cart_shop:cart')



#wishlist

class ViewWishlist(View):
   def get(self, request):
       if request.user.is_authenticated:
           data = Wishlist.objects.filter(cart__user=request.user)
           context = {'data': data}

           return render(request, 'cart_shop/wishlist.html', context)

       return redirect('auth_shop:login')


class ViewWishlistDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(Wishlist, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:wishlist')


class ViewWishlistAdd(View):
   def get(self, request, product_id):
       if request.user.is_authenticated:
           product = get_object_or_404(SingleProduct, id=product_id)
           cart_user = get_object_or_404(CartUser, user=request.user)
           cart_item = Wishlist(cart=cart_user, product=product)
           cart_item.save()
           return redirect('home:index')
       return redirect('auth_shop:login')
