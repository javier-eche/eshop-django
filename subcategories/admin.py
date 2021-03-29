from django.contrib import admin
from .models import Subcategory

@admin.register(Subcategory)

class DisplayCategories(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)
