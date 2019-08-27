from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from .forms import LoginForm, RegistrationForm, ForgotPassForm


def home_page(request):
    return render(request, 'home/index.html')


class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', context={
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', '')
            )
            if user is not None:
                login(request, user)
                return redirect('user_url', username=form.cleaned_data.get('username'))
            else:
                return redirect('login_url')
        return redirect('home_url')


class RegisterUser(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'auth/registration.html', context={
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


class ForgotPass(View):
    def get(self, request):
        form = ForgotPassForm()
        return render(request, 'auth/forgot_pass.html', context={
            'form': form
        })

    def post(self, request):
        return redirect('login_url')


def about(request):
    return render(request, 'about/about.html')
