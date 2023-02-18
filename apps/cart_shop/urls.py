from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewWishlistDel

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),

   path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
   path('wishlist/del/<int:item_id>/', ViewWishlistDel.as_view(), name='remove_item'),

]
