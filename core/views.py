from django.shortcuts import render

from .models import Product
from .forms import ProductModelForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

def product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            print('Form is valid')
            form.save()
            msg = 'Product created successfully'
        else:
            msg = 'Form is not valid'
            print('Form is not valid')
            
        print(f'Está sendo POST: {request.POST}')
    else:
        form = ProductModelForm()

    context = {
        'form': form,
        'msg': msg
    }
    return render(request, 'product.html', context)