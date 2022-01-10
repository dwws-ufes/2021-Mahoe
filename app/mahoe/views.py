from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
import urllib.request
import json

def home(request):
    # Grab Crypto Price Data
    price_request = urllib.request.urlopen("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=BRL")
    price = json.load(price_request)
    # Grab Crypto News
    api_request = urllib.request.urlopen("https://min-api.cryptocompare.com/data/v2/news/?lang=PT")
    api = json.load(api_request)
    return render(request, 'home.html', {'api': api, 'price': price})

@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'mahoe/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'mahoe/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'mahoe/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'mahoe/edit.html', context=context)
