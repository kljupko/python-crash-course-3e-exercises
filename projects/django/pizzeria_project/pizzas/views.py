from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    """The home page for the pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """The page listing the pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Shows info about a single pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)