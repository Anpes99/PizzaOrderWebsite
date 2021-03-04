from django.db import models

# Create your models here.
class PizzaIngredient(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"

class Pizza(models.Model):
	S="SMALL"
	M="MEDIUM"
	SIZE_CHOICES = (
		(S, "Small"),
		(M, "Medium")
	)
	Regular="Regular"
	Sicilian="Sicilian"
	TYPES = (
		(Regular, "Regular"),
		(Sicilian, "Sicilian")
	)	

	ingredients = models.ManyToManyField(PizzaIngredient, blank=True, related_name="pizzas")
	size = models.CharField(max_length=1, choices=SIZE_CHOICES)
	pizzaType = models.CharField(max_length=10, choices=TYPES)
	price = models.CharField(max_length=5)
	def __str__(self):
		return f"Regular pizza {self.size} {self.ingredients}"
		
class SubIngredient(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"

class Sub(models.Model):
	S="SMALL"
	M="MEDIUM"
	SIZE_CHOICES = (
		(S, "Small"),
		(M, "Medium")
	)
	size = models.CharField(max_length=1, choices=SIZE_CHOICES)
	ingredients = models.ManyToManyField(SubIngredient, blank=True, related_name="pizzas")
	price = models.CharField(max_length=5)
	def __str__(self):
		return f"Sub sandwich - {self.size} - {self.Ingredients}"
	


class Order(models.Model):
	pizza = models.ManyToManyField(Pizza, blank=True, related_name="pizzaOrders")
	sub = models.ManyToManyField(Sub, blank=True, related_name="subOrders")
	price = models.CharField(max_length=10)
	def __str__(self):
		return f"Order {self.id} - {self.pizza} - {self.sub}"