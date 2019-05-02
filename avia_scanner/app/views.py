import time
import random
import json

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache
from django.core.serializers import serialize


from .models import City
from .forms import SearchTicket





class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """ request предлагающий города для автоподстановки, возвращает JSON"""

    cache.set('cities', City.objects.all().order_by('name'), 3600)
    cities_cache = cache.get('cities')
    cities_json = serialize('json', cities_cache)
    cities = json.loads(cities_json)
    results = []

    for city in cities:
        if city['fields']['name'][0:len(request.GET['term'])] == request.GET['term']:
            results.append({'value': city['fields']['name']})
    return JsonResponse(results, safe=False)



