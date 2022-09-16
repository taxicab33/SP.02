from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.TextInput(
            attrs={'class': 'input-group inputs mb-2 mt-2'}
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'input-group inputs mb-2 mt-2'}
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={'class': 'input-group inputs mb-2 mt-2'}
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'input-group inputs mb-2 mt-2'}
        )
    )
    surname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}))
    last_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={'class': 'input-group inputs mb-2 mt-2'}
        )
    )

    class Meta:
        model = User
        fields = ('email',
                  'password1',
                  'password2',
                  'first_name',
                  'surname',
                  'last_name')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'input-group inputs mb-2 mt-2'}))