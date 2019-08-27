from django.urls import path, include
from django.contrib import admin
from .views import *

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', home_page, name='home_url'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('user/', include('account.urls')),
    path('shop/', include('shop.urls')),
    path('login/', LoginUser.as_view(), name='login_url'),
    path('registration/', RegisterUser.as_view(), name='registration_url'),
    path('logout/', LogoutUser.as_view(), name='logout_url'),
    path('forgot/', ForgotPass.as_view(), name='forgot_url'),
    path('about/', about, name='about_url')
]
