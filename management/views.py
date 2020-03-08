from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dish, Sales
from . import forms
from datetime import datetime, timedelta, time, date

today = datetime.now().date()
today_day = int(today.strftime("%d"))
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())
this_week = int(today.strftime("%V")) 


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
    if request.method == 'POST':
        ran = 1
        form = forms.Menu_Item_Entry(request.POST, request.FILES)
        instance =form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.info(request, 'saved!')
        return redirect('management:shalominfo')
    form = forms.Menu_Item_Entry()
    #get sales for today
    all_sales = Sales.objects.all()
    #find sales & cash that day
    today_sales = Sales.objects.filter(date=today)
    today_sales_ttl = len(today_sales)
    today_cash = 0
    for sale in today_sales:
        today_cash = today_cash+(sale.price * sale.how_many) 

    #find total sales & cash that week
    this_week_sales = []
    this_week_cash = 0
    for sale in all_sales:
        if int(sale.time_of_sale.strftime("%V")) == this_week:
            this_week_sales.append(sale)
    for sale in this_week_sales:
        this_week_cash = this_week_cash+(sale.price * sale.how_many) 
    #get users signed in today
    users = User.objects.all()
    customers_today = []
    for user in users:
        if int(user.date_joined.strftime("%d")) == today_day:
            customers_today.append(user)
    new_customers_today = len(customers_today)
    print(type(new_customers_today))
    #get users signed in this week &total users
    customers_this_week = []
    for user in users:
        if int(user.date_joined.strftime("%V")) == this_week:
            customers_this_week.append(user)
    new_customers_this_week = len(customers_this_week)

  
    return render(request, 'management/main.html', {'today_cash' : today_cash, 'today_sales' : today_sales, 'this_week_cash' : this_week_cash, 'this_week_sales' : this_week_sales, 'customers_today' : new_customers_today, 'customers_this_week' : new_customers_this_week, 'form' : form})