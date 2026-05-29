from django.contrib import admin

from .models import Product

class AdminPrduct(admin.ModelAdmin):
    list_display = ('title', 'stock')

admin.site.register(Product)