from django.contrib import admin
from .models import Pizza,PizzaIngredient,Sub,SubIngredient,Order
# Register your models here.

admin.site.register(Pizza)
admin.site.register(PizzaIngredient)
admin.site.register(Sub)
admin.site.register(SubIngredient)
admin.site.register(Order)