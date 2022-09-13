from django.contrib import admin

from .models import order_products, orders, products

# Register your models here.

admin.site.register(products)
admin.site.register(order_products)
admin.site.register(orders)
