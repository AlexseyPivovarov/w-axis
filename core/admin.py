from django.contrib import admin
from .models import Product, Cart


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    fields = ('name', 'price')
    list_display = ('name', 'price', 'id')



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('data',)
    filter_horizontal = ('product',)
    # list_display = ('product', 'data')