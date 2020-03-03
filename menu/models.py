from django.db import models
from django.contrib.auth.models import User
import datetime

class Dish(models.Model):
    item_name = models.CharField(max_length=120)
    price = models.IntegerField(editable=True, default=100)
    image = models.ImageField(blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item_name} @ {self.price}'

class Sales(models.Model):
    item_name = models.CharField(max_length=120)
    price = models.IntegerField(editable=True, default=100)
    time_of_sale = models.DateField(auto_now=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.item_name} @ {self.price}'

    

