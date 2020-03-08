from django import forms
from . import models

class Menu_Item_Entry(forms.ModelForm):
    class Meta:
        model = models.Dish
        fields = ["item_name", "price", "image"]

class Sale_Number(forms.ModelForm):
    class Meta:
        model = models.Sales
        fields = ['how_many']