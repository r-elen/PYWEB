from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, remove_item_wishlist, update_item_wishlist, checkout_wishlist

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
   path('wishlist/update_item/<int:item_id>/', update_item_wishlist, name='update_item'),
   path('wishlist/remove_item/<int:item_id>/', remove_item_wishlist, name='remove_item'),
   path('wishlist/checkout/', checkout_wishlist, name='checkout'),
]
