from django.shortcuts import render, redirect
from .models import Dish, Sales
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from datetime import datetime, timedelta, time, date


today = datetime.now().date()
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())


def index(request):
    return render(request, 'menu/index.html')

@login_required(login_url='/a/aio/')
def menu(request):
    return render(request, 'menu/order.html')

@login_required(login_url='/a/aio/')
def order(request, pk=None):
    dish = Dish.objects.all()
    # for i in dish:
    #     print(i.item_name)
    if pk:
        print('order active')
        dish = Dish.objects.filter(pk=pk)
        return render(request, 'menu/order.html', { 'dishs' : dish })
        
    return render(request, 'menu/orders.html', { 'dishs' : dish })

@login_required(login_url='/a/aio/')
def make_order(request, pk=None):
    print('make order active')
    dish = Dish.objects.filter(pk=pk)
    form = forms.Sale_Number()
    if request.method == 'POST':
        started = 'yes'
        form = forms.Sale_Number(request.POST)
        sale = form.save(commit=False)
        item = Dish.objects.filter(pk=pk)
        print('im here now')
        for data in item:
            price = data.price
            name = data.item_name

        sale.user = request.user
        sale.price = price
        sale.item_name = name
        sale.save()
        message = f'you have purchased {sale.how_many} {sale.item_name}'
        messages.info(request, f'you have purchased {sale.how_many}{sale.item_name}')
        # return redirect('menu:mk_order', pk=pk)
        return render(request, 'menu/order.html', { 'dishs' : dish, 'form' : form, 'message' : message, 'started' : started })

    
    return render(request, 'menu/order.html', { 'dishs' : dish, 'form' : form })

@login_required(login_url='/a/aio/')
def menu_modify(request):
    if request.method == 'POST':
        form = forms.Menu_Item_Entry(request.POST, request.FILES)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.info(request, 'saved!')
        return redirect('menu:menumod')
    form = forms.Menu_Item_Entry()
    
    return render(request, 'menu/menumod.html', {'form' : form})

