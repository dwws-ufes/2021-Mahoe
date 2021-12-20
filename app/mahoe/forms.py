from django.contrib.auth.models import User
from django import forms
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm


class UserRegistration(forms.ModelForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput)
    first_name = forms.CharField(label='Nome', widget=forms.TextInput)
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repita Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


