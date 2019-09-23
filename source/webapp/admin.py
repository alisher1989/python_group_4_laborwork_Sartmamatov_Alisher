from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'category', 'amount', 'price']
    list_filter = ['name']
    list_display_links = ['pk', 'description']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'amount', 'price']
    # readonly_fields = ['amount', 'price']


admin.site.register(Product, ProductAdmin)

