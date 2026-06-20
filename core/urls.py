from django.urls import path

from .views import index,contact,product, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('listproduct/', ProductListView.as_view(), name='listProd'),
    path('createproduct/', ProductCreateView.as_view(), name='createProd'),
    path('updateproduct/<int:pk>/', ProductUpdateView.as_view(), name='updateProd'),
    path('deleteproduct/<int:pk>/', ProductDeleteView.as_view(), name='deleteProd')
]