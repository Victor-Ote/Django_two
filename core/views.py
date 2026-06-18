from django.shortcuts import render

from .models import Product
from .forms import ProductModelForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

def product(request):
    msg = ''
    if request.method == 'POST':
        
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = 'Product created successfully'
        else:
            msg = 'Form is not valid'
            print('Form is not valid')
        form.clean()
        print(f"Requisição:{request.POST.get('action')}")

    else:
        form = ProductModelForm()

    context = {
        'form': form,
        'msg': msg,
        'products': Product.objects.all()
    }
    return render(request, 'product.html', context)