from django.contrib import admin
from .models import Product

@admin.register(Product)  # This is a simpler way to register the model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'quantity', 'price')
    search_fields = ('name',)
    list_filter = ('quantity', 'price')

