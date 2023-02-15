from django.urls import path
from .views import ViewCart, ViewProductSingle

app_name = 'shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='shop'),
   path('product-single/', ViewProductSingle.as_view(), name='product-single'),

]
