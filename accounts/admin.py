"""
Accounts admin
"""
###
# Libraries
###
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'username', 'is_active', 'last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'address', 'stripe_id', 'mobile_country_code', 'mobile_phone_number',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(models.ChangeEmailRequest)
class ChangeEmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email',)
    readonly_fields = ('uuid',)
