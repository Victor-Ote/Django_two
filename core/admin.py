from django.contrib import admin

from .models import Product

@admin.register(Product)
class AdminPrduct(admin.ModelAdmin):
    list_display = ('title', 'stock', 'slug')