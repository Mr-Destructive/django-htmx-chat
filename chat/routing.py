from django.urls import path

from chat import consumers

websocket_urlpatterns = [
    path('chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
