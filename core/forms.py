from .models import Product
from django import forms

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'sku', 'stock', 'price', 'description', 'image']