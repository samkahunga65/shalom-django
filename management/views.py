from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dish, Sales
from . import forms
from datetime import datetime, timedelta, time, date

today = datetime.now().date()
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())

def management_login(request):
    if request.method == 'POST':
        form = forms.Menu_Item_Entry(request.POST, request.FILES)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.info(request, 'saved!')
        return redirect('management:login')
    form = forms.Menu_Item_Entry()
    # sales = Sales.objects.filter(date.today())
    return render(request, 'menu/index.html', {'form' : form})

@login_required(login_url='/a/login')
def menu_modify(request):
    if request.method == 'POST':
        form = forms.Menu_Item_Entry(request.POST, request.FILES)
        instance =form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.info(request, 'saved!')
        return redirect('management:menumod')
    form = forms.Menu_Item_Entry()
    # sales = Sales.objects.filter(date.today())
    return render(request, 'management/menumod.html', {'form' : form})

def shalom_info(request):
    #get sales for today
    sales = Sales.objects.filter(time_of_sale=today)
    for sale in sales:
        print(sale)
        
    #get users signed in today
    return render(request, 'management/main.html')