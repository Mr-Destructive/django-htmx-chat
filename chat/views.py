from django.shortcuts import render, reverse, redirect
from chat.models import Room

def index(request, name):
    room = Room.objects.get(slug=name)
    return render(request, 'room.html', {'name': room.name, 'slug': room.slug})

def room_create(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        room_slug= room_name.replace(' ', '_').replace("'", "_")
        room = Room.objects.create(name=room_name, slug=room_slug)
        return redirect(reverse('chat', kwargs={'name': room.slug}))
    else:
        return render(request, 'room.html')

def room_join(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        room = Room.objects.get(name=room_name)
        return redirect(reverse('room', kwargs={'name': room.slug}))
    else:
        return render(request, 'join.html')
