from django.shortcuts import render
from django.http import HttpResponse

from .models import Order,Drink,Names,Extras
# Create your views here.

def main(request):
    if request.method == 'POST':
        name = request.POST['name']
        order = request.POST['order']
        extra = request.POST['extras']
        sugar = request.POST['sugar']

        new_order = Order(name = name, order = order, extras = extra, sugar = sugar)
        new_order.save()

    names = Names.objects.all()
    drinks = Drink.objects.all()
    extras = Extras.objects.all()
    return render(request, 'index.html', {'names': names, 'drinks': drinks, 'extras' : extras})

def view_orders(request):
    orders = Order.objects.all()
    
    return render(request, 'view_orders.html', {'orders': orders})
    # return render(request,'view_orders.html')


def admin_page(request):
    drinks = Drink.objects.all()  # Fetch the list of drinks from your model
    context = {'drinks': drinks}
    return render(request, 'admin_page.html', context)