from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from chat.models import Room

def index(request, name):
    room = Room.objects.get(slug=name)
    return render(request, 'chat/room.html', {'name': room.name, 'slug': room.slug})

@login_required
def room_create(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        room_slug= room_name.replace(' ', '_').replace("'", "_")
        room = Room.objects.create(name=room_name, slug=room_slug)
        return redirect(reverse('chat', kwargs={'name': room.slug}))
    else:
        return render(request, 'chat/create.html')

@login_required
def room_join(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        room = Room.objects.get(name=room_name)
        return redirect(reverse('chat', kwargs={'name': room.slug}))
    else:
        return render(request, 'chat/join.html')
