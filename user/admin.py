from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class UserDetailsAdmin(UserAdmin):
    """
    Custom admin for User model
    """

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                    "is_active",
                    "bio",
                )
            },
        ),
    )

    list_display = (
        "id",
        "email",
        "username",
        "is_active",
    )
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, UserDetailsAdmin)
