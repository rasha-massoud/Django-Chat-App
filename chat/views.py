from django.shortcuts import render, redirect
from chat.models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html', {'room': room})

def checkview(request):
    room = request.POST['room']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        redirect('/'+room+'/?username'+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        redirect('/'+room+'/?username'+username)