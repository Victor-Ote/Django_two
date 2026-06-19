from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductModelForm


from django.views.generic import ListView, CreateView

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



#CRUD with CBV

#READ
class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'listProd.html'
    
#CREATE
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('core:listProd')
    template_name = 'createProd.html'