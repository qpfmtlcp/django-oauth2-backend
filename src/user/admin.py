from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'email', 'is_active', 'created',)
    list_display_links = ('name', 'email',)
    list_filter = ('is_active', 'is_staff', 'created',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (None, {'fields': ('last_login', 'created',)}),
        (None, {'fields': ('is_active', 'is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('last_login', 'created',)
    ordering = ('name', 'created',)


admin.site.unregister(Group)
admin.site.register(get_user_model(), CustomUserAdmin)
