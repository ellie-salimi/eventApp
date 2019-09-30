from django.shortcuts import render
from .models import Event


def index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)

def event(request, event_id):
    return render(request, 'events/event.html')


def search(request):
    return render(request, 'events/search.html')