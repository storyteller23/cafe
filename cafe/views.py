from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

def index(request):
    context = {}
    context['menu'] = Menu.objects.all()
    context['orders'] = Order.objects.all()
    return render(request, 'cafe/index.html', context=context)


def orders(request):
    context = {}
    context['orders'] = Order.objects.all()
    return render(request, 'cafe/orders.html', context=context)


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            dishes = form.cleaned_data.get("dishes")
            client_name = form.cleaned_data.get("client_name")
            served_employee = form.cleaned_data.get("served_employee")
            total_price = 0
            for dish in dishes:
                total_price += dish.price
            order = Order(client_name=client_name, served_employee=served_employee, total_price=total_price)
            order.save()
            order.dishes.set(dishes)
            return redirect('/orders')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'cafe/create_order.html', context)