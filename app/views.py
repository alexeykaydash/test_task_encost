from django.shortcuts import render
from django.db.models import F
from django.views.generic import View
from app.models import Clients, Durations, Equipment, Modes


class BlogListView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        if args:
            context['query'] = args[1]['query']
        context['clients'] = Clients.objects.all()
        context['equipments'] = Equipment.objects.all()
        context['modes'] = Modes.objects.all()
        return render(request, 'index.html', {'context': context})

    def post(self, request):
        query = Durations.objects.all()

        client = request.POST.get('client')
        equipment = request.POST.get('equipment')
        mode = request.POST.get('mode')
        minutes = request.POST.get('minutes')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        if client != 'Все':
            query = query.filter(client__name=client)
        if equipment != 'Все':
            query = query.filter(equipment__name=equipment)
        if mode != 'Все':
            query = query.filter(mode__name=mode)
        if minutes:
            query = query.filter(minutes__gte=minutes)
        if start_date:
            query = query.filter(start__startswith=start_date)
        if end_date:
            query = query.filter(stop__startswith=end_date)
        if start_time:
            query = query.filter(start__regex=fr".{{11}}{start_time[:2]}.{{6}}")
        if end_time:
            query = query.filter(start__regex=fr'.{{11}}{end_time[:2]}.{{6}}')
        return self.get(request, 'index.html', {'query': query})



