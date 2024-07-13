from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'form/index.html')
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        new_product = Product(name=name, price=price, description=description)
        new_product.save()
        success = 'product "'+name+'" created successfully'
        return redirect('/orders/', success=success)
    