from django.contrib import admin
from .models import Product

@admin.register(Product)

class DisplayProducts(admin.ModelAdmin):
    list_display = ('pk', 'name','brand',)
    list_display_links = ('pk', 'name','brand',)

    search_fields = (
        'name',
        'brand',
    )

    list_filter = (
        'name',
        'brand',
    )