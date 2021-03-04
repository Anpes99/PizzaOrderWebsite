from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import PizzaIngredient,Pizza,SubIngredient,Sub,Order
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html")

	else: 
		if not "shoppingCart" in request.session:
			request.session['shoppingCart']=[]
		context={"pizzaIngredients": PizzaIngredient.objects.all(),
				"subIngredients":SubIngredient.objects.all()}
		return render(request, "orders/index.html", context)

def register1(request):
	if not request.user.is_authenticated:
		return render(request, "orders/register1.html")

	else: 
		if not request.session['shoppingCart']:
			request.session['shoppingCart']=[]
		context={"pizzaIngredients": PizzaIngredient.objects.all(),
				"subIngredients":SubIngredient.objects.all()}
		return render(request, "orders/index.html", context)

def register(request):
	if request.user.is_authenticated:
		return render(request, "orders/index.html")
	username1 = request.POST.get("username1")
	password1 = request.POST.get("password1")
	if username1 != None:
		user = User.objects.create_user(username=username1, email=None, password=password1)
		user.save()
		user1 =authenticate(request, username=username1, password=password1)
		login(request, user1)
		context={"pizzaIngredients": PizzaIngredient.objects.all(),
				"subIngredients":SubIngredient.objects.all()
		}
		return render(request, "orders/index.html", pizzaIngredients)
	else :
		return render(request, "orders/index.html")

def loginuser(request):
	username = request.POST.get("username1")
	password = request.POST.get("password1")
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		if not request.session['shoppingCart']:
			request.session['shoppingCart']=[]
		context={"pizzaIngredients": PizzaIngredient.objects.all(),
				"subIngredients":SubIngredient.objects.all()}
		return render(request, "orders/index.html", pizzaIngredients)
	else: 
		if not request.session['shoppingCart']:
			request.session['shoppingCart']=[]
		return render(request, "orders/login.html")

def confirmCart(request):
	return render(request,"orders/placeOrder.html")


#  Takes items from shopping cart and creates an order object ---> completes the order
#  Problem with csrf certification
def orderConfirmed(request):
	print("@@@@STARTING ORDERCONFIRMED@@@@@@@@@@@@@@@@@@@@@@@")
	order1 = Order()
	order1.save()
	price=0
	
	shoppingCart = request.session['shoppingCart']
	print(shoppingCart)
	print("@@@@STARTING FOR LOOP@@@@@@@@@@@@@@@@@@@@@@@")
	for i in range(0,len(shoppingCart)):
		if (shoppingCart[i]["typ"] == 'sub'):
			
			sub1=Sub(size=shoppingCart[i]["size"],price=shoppingCart[i]["price"])
			sub1.save()
			sub1.ingredients.add(SubIngredient.objects.get(name=shoppingCart[i]["ing1"]))
			
			order1.sub.add(sub1)
			
			price+=float(shoppingCart[i]["price"])
			success =True
		else:
			pizza1 = Pizza(size=shoppingCart[i]["size"],pizzaType=shoppingCart[i]["typ"],price=shoppingCart[i]["price"])
			pizza1.save()
			pizza1.ingredients.add(PizzaIngredient.objects.get(name=shoppingCart[i]["ing1"]))
			pizza1.ingredients.add(PizzaIngredient.objects.get(name=shoppingCart[i]["ing2"]))
			pizza1.ingredients.add(PizzaIngredient.objects.get(name=shoppingCart[i]["ing3"]))
			order1.pizza.add(pizza1)
			
			price+=float(shoppingCart[i]["price"])
			success=True
	print("@@@@FOR LOOP DONE@@@@@@@@@@@@@@@@@@@@@@@")
	setattr(order1, 'price', price)
	order1.save()
	print("@@@@@@@@@@@@@@@@@@DONE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	return render(request, 'orders/index.html')
	return JsonResponse({"success": True})#,  RequestContext(request)
	
def addItem(request):
	if not request.session['shoppingCart']:
		request.session['shoppingCart']=[]
	shoppingCart = request.session['shoppingCart']
	ing1 = request.POST.get("ing1")
	ing2 = request.POST.get("ing2")
	ing3 = request.POST.get("ing3")
	size = request.POST.get("size")
	typ =request.POST.get("type")
	price = request.POST.get("price")
	if (typ == "pizza"):
		pizza = {}
		pizza["ing1"]=ing1
		pizza["ing2"]=ing2
		pizza["ing3"]=ing3
		pizza["size"]=size
		pizza["typ"]=typ
		pizza["price"]=price
		shoppingCart.append(pizza)
		request.session['shoppingCart']=shoppingCart
		success=True
		return JsonResponse({"success": success})
	if (typ == "sub"):
		sub = {}
		sub["ing1"]=ing1
		sub["size"]=size
		sub["typ"]=typ
		sub["price"]=price
		shoppingCart.append(sub)
		request.session['shoppingCart']=shoppingCart
		success=True
		return JsonResponse({"success": success})