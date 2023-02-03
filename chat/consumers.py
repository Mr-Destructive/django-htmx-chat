import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.user = self.scope["user"]

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.user.username
        room = self.room_name
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat_message",
                "message": message,
                "room": room,
                "username": username,
            }
        )

    def chat_message(self, event):
        message = event["message"]
        room = event["room"]
        username = event["username"]

        message_html = f"""
        <div hx-swap-oob='beforeend:#notifications'>
            <p><b>{username}</b>: {message}</p>
        </div>
        """
        self.send(
            text_data=json.dumps(
                {
                    "message": message_html,
                    "room": room,
                    "username": username
                }
            )
        )
