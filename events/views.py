from django.shortcuts import get_object_or_404, render
from .models import Event


def index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event' : event
    }

    return render(request, 'events/event.html', context)


def search(request):
    return render(request, 'events/search.html')