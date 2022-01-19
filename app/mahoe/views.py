from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserEditForm
import urllib.request
import json

def home(request):
    # prices
    price_request = urllib.request.urlopen("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=BRL")
    price = json.load(price_request)
    # news
    news_request = urllib.request.urlopen("https://min-api.cryptocompare.com/data/v2/news/?lang=PT")
    news = json.load(news_request)
    news['Data'] = news['Data'][:12]
    return render(request, 'home.html', {'news': news, 'price': price})

@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'mahoe/templates/authapp/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'mahoe/templates/authapp/register_done.html')
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, 'mahoe/templates/authapp/register.html', context=context)


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
    return render(request, 'mahoe/templates/authapp/edit.html', context=context)
