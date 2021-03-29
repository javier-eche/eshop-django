from django.contrib import admin
from .models import Category

@admin.register(Category)

class DisplaysubCategories(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)