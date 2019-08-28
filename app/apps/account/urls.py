from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_to_user),
    path('<username>/', show_user, name='user_url'),
]
