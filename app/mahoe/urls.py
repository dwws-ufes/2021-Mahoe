from django.urls import path, include
from django.views.generic.base import View
from .views import edit, dashboard, home, register
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'mahoe'

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='mahoe/templates/authapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='mahoe/templates/authapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='mahoe/templates/authapp/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='mahoe/templates/authapp/password_change_done.html'),
         name='password_change_done'),
]
