from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_superuser", "is_staff")
    search_fields = (
        "username",
        "email",
    )
    list_filter = ("is_superuser", "is_staff")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
