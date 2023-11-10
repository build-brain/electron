from django.contrib import admin
from management.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )
    list_filter = "is_staff", "is_superuser", "is_active",
    search_fields = ("phone_number", "first_name", "last_name", "email")
    ordering = "phone_number",
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_display = "phone_number", "registered_at"
