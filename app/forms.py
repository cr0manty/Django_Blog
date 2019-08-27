from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    def get_user(self):
        user = User(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name')
        )
        user.set_password(self.cleaned_data.get('password'))
        return user

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'username', 'email',
            'password'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

        labels = {
            'first_name': 'Фамилия',
            'last_name': 'Имя',
            'email': 'Email',
            'username': 'Логин',
            'password': 'Пароль',
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    error_messages = {
        'invalid_login': (
            'Please enter a correct %(username)s and password. Note that both '
            'fields may be case-sensitive.'
        ),
        'inactive': ('This account is inactive.')
    }


class ForgotPassForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    new_password = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

