from django.contrib import admin

from management.models import AuthUser


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = "email", "display_name", "created_at"

