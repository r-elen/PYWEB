from django.urls import path
from .views import ViewCart, ViewProductSingle, ViewWishlist

app_name = 'shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='shop'),
   path('', ViewProductSingle.as_view(), name='product-single'),
   path('', ViewWishlist.as_view(), name='wishlist'),

]
