from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout, login
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from .forms import *


def home_page(request):
    return render(request, 'home/index.html')


#TODO ошибка в случае ошибки
class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'home/auth/login.html', context={
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd.get('username', ''),
                password=cd.get('password', '')
            )
            if user is not None:
                login(request, user)
                return redirect('user_url', cd.get('username'))
            else:
                return redirect('login_url')
        return redirect('home_url')


#TODO ошибка в случае ошибки
class RegisterUser(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'home/auth/registration.html', context={
            'form': form
        })

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            user.save()
            return redirect('login_url')
        return redirect('registration_url')


class LogoutUser(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        logout(request)
        return redirect('home_url')


#TODO ошибка в случае ошибки
class ForgotPass(View):
    def get(self, request):
        form = ForgotPassForm()
        return render(request, 'home/auth/forgot_pass.html', context={
            'form': form
        })

    def post(self, request):
        form = ForgotPassForm(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                user = User.objects.get(
                    email=cd.get('email'),
                    username=cd.get('username'),
                )
            except:
                return redirect('login_url')
            if User is not None:
                if cd.get('new_password') ==\
                        cd.get('new_password2'):
                    user.set_password(cd.get('new_password'))
                    user.save()
        return redirect('login_url')


def about(request):
    return render(request, 'home/about.html')
