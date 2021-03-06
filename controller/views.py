from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import events

# Create your views here.


registry = events.EventRegistry()


def main(request):
    return render(request, 'controller/main.html')


def event(request):
    event = registry.event_dict.get(request.GET.get('type', None))
    trig = request.GET.get('trig', None)
    value = request.GET.get('value', None)

    if event is None or trig is None:
        raise Http404
    else:
        if trig == 'down':
            event.trig_on()
        elif trig == 'up':
            event.trig_off()

        return HttpResponse("")