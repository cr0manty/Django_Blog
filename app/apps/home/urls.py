

from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home_url'),
    path('login/', LoginUser.as_view(), name='login_url'),
    path('registration/', RegisterUser.as_view(), name='registration_url'),
    path('logout/', LogoutUser.as_view(), name='logout_url'),
    path('forgot/', ForgotPass.as_view(), name='forgot_url'),
    path('about/', about, name='about_url'),
]
