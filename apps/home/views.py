from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


class IndexShopView(View):
   def get(self, request):
       return render(request, 'home/index.html')

class ViewAboout(View):
   def get(self, request):
       return render(request, 'home/about.html')

class ViewContact(View):
   def get(self, request):
       return render(request, 'home/contact.html')
