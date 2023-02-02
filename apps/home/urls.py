from django.urls import path

from .views import IndexShopView, ViewAboout, ViewContact

app_name = 'home'

urlpatterns = [
   path('', IndexShopView.as_view(), name='index'),
   path('', ViewAboout.as_view(), name='about'),
   path('', ViewContact.as_view(), name='contact'),
]

