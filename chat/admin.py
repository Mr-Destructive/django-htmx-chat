from django.contrib import admin

from chat.models import Message
from chat.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    search_fields = (
        "name",
        "slug",
    )
    filter_horizontal = ("users",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]
    
    list_display = (
        "room",
        "user",
        "message",

    )
    search_fields = (
        "room",
        "user",
        "message",
    )
    list_filter = (
        "room",
        "user",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "room",
                    "user",
                    "message",
                    "created_at",
                )
            },
        ),
    )
