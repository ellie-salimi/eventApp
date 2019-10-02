from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event, Category


def index(request):
    events = Event.objects.order_by('-end_time')[:3]
    categories = Category.objects.all

    context = {
        'events': events,
        'categories': categories
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')


