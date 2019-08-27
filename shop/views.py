from django.shortcuts import render


def shop_home(request):
    return render(request, 'shop/shop_home.html')
