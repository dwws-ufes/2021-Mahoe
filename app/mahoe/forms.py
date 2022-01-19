from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean_password2(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password is not None and password != password2:
            self.add_error("password22", "Your passwords must match")
        return cleaned_data

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


