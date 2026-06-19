from django.urls import path

from .views import index,contact,product, ProductListView, ProductCreateView

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('listproduct/', ProductListView.as_view(), name='listProd'),
    path('createproduct/', ProductCreateView.as_view(), name='createProd')
]