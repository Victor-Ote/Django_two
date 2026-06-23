from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductModelForm


from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
    
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            print(f"User logado: {request.user}")
        else:
            print("User não logado")
        print("Entrou na view")
        return super().dispatch(request, *args, **kwargs)

#CREATE
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('core:listProd')
    template_name = 'createProd.html'
    
    def post(self, request, *args, **kwargs):

        print(f"User logado: {request.user}")

        return super().post(request, *args, **kwargs)

#UPDATE
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('core:listProd')
    template_name = 'createProd.html'

#DELETE
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('core:listProd')
