from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewWishlistDel, ViewCartAdd, ViewWishlistAdd, \
   update_item, checkout_cart

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
   path('update_item/<int:item_id>/', update_item, name='update_item'),
   # path('view_cart_total/<int:item_id>/', view_cart_total, name='remove_item'),
   path('checkout/', checkout_cart, name='checkout'),

   path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
   path('wishlist/del/<int:item_id>/', ViewWishlistDel.as_view(), name='del_from_wishlist'),
   path('wishlist/add/<int:product_id>/', ViewWishlistAdd.as_view(), name='add_to_wishlist'),

]
