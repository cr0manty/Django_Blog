from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('account.urls')),
    path('shop/', include('shop.urls')),
]
