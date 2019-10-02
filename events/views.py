from django.shortcuts import get_object_or_404, render
from .models import Event,Category



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
    queryset_list = Event.objects.all
    categories = Category.objects.all

    #keywords
    # if 'keywords' in request.GET :
    #     keywords = request.GET['keywords']
    #     if keywords:
    #         queryset_list = queryset_list.filter(description__icontains=keywords)
    
     # Category
    # if 'categories' in request.GET:
    #     category = request.GET['category']
    # if category:
    #   queryset_list = queryset_list.filter(categories__iexact=category)

    context ={
        'categories': categories,
        'events': queryset_list,
        'values': request.GET
    }
    return render(request, 'events/search.html', context)