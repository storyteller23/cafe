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
            form.save()
            return redirect('/orders')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'cafe/create_order.html', context)