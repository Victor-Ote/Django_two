from django.shortcuts import render

from .models import Product

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

def product(request):
    if request.method == 'POST':
        print(request.POST)
    
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product.html', context)