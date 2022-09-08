from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Product, Category, OrderItem, ShippingAddress, Order, ProductSearch
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ProductSearch)
