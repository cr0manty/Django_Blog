from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post


def show_user(request, username):
    user = get_object_or_404(User, username__iexact=username)
    posts = Post.objects.filter(author_id=user.id)
    return render(request, 'account/user_page.html', context={
        'user': user,
        'posts': posts
    })


def redirect_to_user(request):
    if request.user.is_authenticated:
        return redirect('user_url', username=request.user)
    return redirect('login_url')
