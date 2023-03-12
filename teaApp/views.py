from django.shortcuts import render
from django.http import HttpResponse

from .models import Order
# Create your views here.

def main(request):
    if request.method == 'POST':
        name = request.POST['name']
        order = request.POST['order']
        # date = request.POST['created']


        new_order = Order(name = name, order = order)
        new_order.save() 
    return render(request,'index.html')

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'view_orders.html', {'orders': orders})
    # return render(request,'view_orders.html')
