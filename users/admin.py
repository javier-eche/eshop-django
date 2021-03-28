from django.contrib import admin
from users.models import User

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email',)
    list_display_links = ('pk', 'name', 'email',)

    search_fields = (
        'email',
        'name',
        'dni',
        'phone',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'date_joined',
    )

    readonly_fields = ('date_joined',)