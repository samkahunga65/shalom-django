from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dish, Sales
from . import forms
from datetime import datetime, timedelta, time, date

def management_login(request):
    if request.method == 'POST':
        form = forms.Menu_Item_Entry(request.POST, request.FILES)
        instance =form.save(commit=False)
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
    return render(request, 'menu/menumod.html', {'form' : form})