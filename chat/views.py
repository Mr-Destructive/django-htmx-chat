import random
import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.utils.text import slugify

from chat.models import Room


@login_required
def index(request, slug):
    try:
        room = Room.objects.get(slug=slug)
    except Room.DoesNotExist:
        return render(
            request,
            "chat/join.html",
            {"error": "This room does not exist. Please check the name and try again."},
        )
    return render(request, "chat/room.html", {"name": room.name, "slug": room.slug})


@login_required
def room_create(request):
    if request.method != "POST":
        return render(request, "chat/create.html")

    room_name = request.POST["room_name"]

    try:
        Room.objects.get(name=room_name)
        return render(
            request,
            "chat/create.html",
            {"error": "This room already exists. Please try again."},
        )
    except Room.DoesNotExist:
        pass

    uid = str("".join(random.choices(string.ascii_letters + string.digits, k=4)))
    room_slug = slugify(f"{room_name}_{uid}")
    room = Room.objects.create(name=room_name, slug=room_slug)
    return redirect(reverse("chat", kwargs={"slug": room.slug}))


@login_required
def room_join(request):
    if request.method != "POST":
        return render(request, "chat/join.html")

    room_name = request.POST["room_name"]
    try:
        room = Room.objects.get(slug=room_name)
    except Room.DoesNotExist:
        return render(
            request,
            "chat/join.html",
            {"error": "This room does not exist. Please check the name and try again."},
        )
    return redirect(reverse("chat", kwargs={"slug": room.slug}))
