from django.shortcuts import render

from messenger import models


# Create your views here.


def index(request):
    rooms = models.Room.objects.all()
    room = models.Room.objects.get(slug=1)
    messages = models.Message.objects.filter(room=room)
    return render(request, "index.html", context={"rooms": rooms, "messages":messages})
