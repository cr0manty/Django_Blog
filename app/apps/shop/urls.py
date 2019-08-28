from django.urls import path
from .views import *

urlpatterns = [
    path('', shop_home, name='shop_home_url'),
]
