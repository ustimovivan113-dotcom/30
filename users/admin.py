from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'city', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'city')
    search_fields = ('email', 'username', 'city')
    ordering = ('-id',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('phone', 'city', 'avatar')}),
    )
