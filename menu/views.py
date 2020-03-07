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
        dish = Dish.objects.filter(pk=pk)
        
    return render(request, 'menu/orders.html', { 'dishs' : dish })

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

