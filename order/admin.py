from django.contrib import admin
from .models import Order

@admin.register(Order)

class DisplayOrder(admin.ModelAdmin):
    list_display = ('pk', 'user_name','amount','created_at',)
    list_display_links = ('pk', 'user_name','amount','created_at',)

    search_fields = (
        'user_name',
        'created_at',
    )

    list_filter = (
        'user_name',
        'created_at',
    )