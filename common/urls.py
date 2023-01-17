from django.contrib import admin
from django.urls import path, include

from .views import CurrentDateView, HelloView, IndexView


urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', HelloView.as_view()),
   path('index/', IndexView.as_view()),

]
