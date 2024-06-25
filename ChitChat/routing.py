from django.urls import path, include
from ChitChat.consumer import ChatConsumer

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]

# when a WebSocket connection is made to the application's root URL, it's handled by the ChatConsumer to manage the chat functionality.