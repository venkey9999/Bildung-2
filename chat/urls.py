from django.urls import path
from django.shortcuts import render

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

urlpatterns = [
    path("<str:room_name>/", room, name="room"),
]
