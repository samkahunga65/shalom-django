from django.shortcuts import render, redirect
from .models import Dish
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms


def index(request):
    return render(request, 'menu/index.html')

@login_required(login_url='/a/login')
def menu(request):
    return render(request, 'menu/order.html')

@login_required(login_url='/a/login')
def order(request):
    dish = Dish.objects.all()
    for i in dish:
        print(i.item_name)
    return render(request, 'menu/orders.html', { 'dishs' : dish })

@login_required(login_url='/a/login')
def menu_modify(request):
    if request.method == 'POST':
        form = forms.Menu_Item_Entry(request.POST, request.FILES)
        instance =form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.info(request, 'saved!')
        return redirect('menu:menumod')
    form = forms.Menu_Item_Entry()
    return render(request, 'menu/menumod.html', {'form' : form})

