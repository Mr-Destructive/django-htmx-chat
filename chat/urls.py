from django.urls import path
from chat import views


urlpatterns = [
    path("chat/room/<str:name>/", views.index, name='room'),
    path("create/", views.room_create, name='room-create'),
    path("join/", views.room_join, name='room-join'),
]
