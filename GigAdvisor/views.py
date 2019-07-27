from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from static.fusioncharts import FusionCharts
from static.fusioncharts import FusionTable
from static.fusioncharts import TimeSeries
from collections import OrderedDict
from django.shortcuts import render
from GigAdvisor.forms import ReviewForm
from .models import *
from django.core import serializers
import simplejson
import requests


import json

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def team(request):
    context = {'team_page': "active"}  # new info here
    return render(request, 'team.html', context)
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict



def charts(request):

    dataSource = {}
    dataSource['chart'] = {
        "caption": "Grafico di Rating",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
           
        }
    dataSource['data'] = []

    for key in Platform.objects.all():
      data = {}
      
      data['label'] = key.nome
      data['value'] = simplejson.dumps(key.rating, use_decimal=True)
      dataSource['data'].append(data)


    dataSource1 = {}
    dataSource1['chart'] = {
        "caption": "Sicurezza sul lavoro",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "#0075c2,#1aaf5d,#f2c500",
        }
    dataSource1['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value1 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value1')).get('value1__avg')
        
        data['label'] = plat.nome
        data['value'] = int(avg_value1)
        dataSource1['data'].append(data)
        avg_value1 = 0
        



    dataSource2 = {}
    dataSource2['chart'] = {
        "caption": "Trasparenza del contratto",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "#0075c2,#1aaf5d,#f2c500",
        }
    dataSource2['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value2 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value2')).get('value2__avg')
        data['label'] = plat.nome
        data['value'] = int(avg_value2)
        dataSource2['data'].append(data)

    dataSource3 = {}
    dataSource3['chart'] = {
        "caption": "Tempestività pagamenti",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "#0075c2,#1aaf5d,#f2c500",
        }
    dataSource3['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value3 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value3')).get('value3__avg')
        data['label'] = plat.nome
        data['value'] = int(avg_value3)
        dataSource3['data'].append(data)

    dataSource4 = {}
    dataSource4['chart'] = {
        "caption": "Correttezza del datore di lavoro",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "#0075c2,#1aaf5d,#f2c500",
        }
    dataSource4['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value4 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value4')).get('value4__avg')
        data['label'] = plat.nome
        data['value'] = int(avg_value4)
        dataSource4['data'].append(data)

    column2D = FusionCharts("column2d", "myFirstChart", "100%", "400", "chart-container", "json", dataSource)

    graph1 = FusionCharts("column2d", "myFirstChart1", "100%", "300", "chart1-container", "json", dataSource1)
    graph2 = FusionCharts("column2d", "myFirstChart2", "100%", "300", "chart2-container", "json", dataSource2)
    graph3 = FusionCharts("column2d", "myFirstChart3", "100%", "300", "chart3-container", "json", dataSource3)
    graph4 = FusionCharts("column2d", "myFirstChart4", "100%", "300", "chart4-container", "json", dataSource4)
        
    return render(request, 'charts.html', {'output': column2D.render(), 'output1': graph1.render(), 'output2': graph2.render(), 'output3': graph3.render(), 'output4': graph4.render()})

def home(request):
    context = {'home_page': "active"}  # new info here
    return render(request, 'home.html', context)


class PlatformListView(generic.ListView):
    model = Platform

    context_object_name = 'platforms_list'
    queryset = Platform.objects.all()
    template_name = 'platforms.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlatformListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['platform_page'] = 'active'
        return context

def recensione_new(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            titolo = form.cleaned_data['titolo']
            descrizione = form.cleaned_data['descrizione']
            range1 = int(request.POST['range1'])
            range2 = int(request.POST['range2'])
            range3 = int(request.POST['range3'])
            range4 = int(request.POST['range4'])
            rating = (range1+range2+range3+range4)/4
            platform = Platform.objects.get(id=id)
            platform.rating = rating
            platform.save()
            r = Recensioni(titolo=titolo, descrizione=descrizione,platform=platform, value1=range1, value2=range2, value3=range3, value4=range4)
            r.save()

            return render(request, 'success_review.html')
        else:
            return render(request, 'unsuccess_review.html')
    else:
        form = ReviewForm(request.POST)
        return render(request, 'reviews_form.html', {'form': form})

def success(request):
    return render(request, 'platforms.html')



def andamento_platform (request, id):

    schema_chart = [{
        "name": "Time",
        "type": "date",
        "format": "%d-%b-%y"
        }, {
        "name": "Type",
        "type": "string"
        }, {
        "name": "Sales Value",
        "type": "number"
        }]
    funds = Recensioni.objects.filter(platform__id=id).all()
    data = serializers.serialize("json", funds, fields=('data','value1','value2','value3', 'value4',))
    
    y = json.loads(data)
    
    final_data = []
    from datetime import datetime
    import pytz
    
    for i in range(len(y)):
        z = y[i]
        data = datetime.strptime(z['fields']['data'], "%Y-%m-%dT%H:%M:%S.%f%z")
        data = data.strftime("%d-%b-%y")
        d1 = [data, "Sicurezza sul lavoro", z['fields']['value1']]
        d2 = [data, "Trasparenza del contratto", z['fields']['value2']]
        d3 = [data, "Tempestività dei pagamenti", z['fields']['value3']]
        d4 = [data, "Correttezza del datore di lavoro", z['fields']['value4']]
        final_data.append(d1)
        final_data.append(d2)
        final_data.append(d3)
        final_data.append(d4)

    fusionTable = FusionTable(str(schema_chart), str(final_data))
    
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute('chart', '{}')
    timeSeries.AddAttribute('caption', '{"text":"Sales Analysis"}')
    timeSeries.AddAttribute('subcaption', '{"text":"Grocery & Footwear"}')
    timeSeries.AddAttribute('series', '"Type"')
    timeSeries.AddAttribute('yaxis', '[{"plot":"Sales Value","title":"Sale Value","format":{"prefix":""}}]')
    

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

    
    return render(request, 'andamento_platform.html', {'output5': fcChart.render()})


def recensione_platform (request, id):
    platform = Platform.objects.get(id=id)
    
    recensioni = Recensioni.objects.filter(platform__id=platform.id).values()
    avg_value1 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value1'))
    avg_value2 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value2'))
    avg_value3 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value3'))
    avg_value4 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value4'))

    context = {
        'platform': platform,
        'recensioni': recensioni,
        'avg_value1': avg_value1,
        'avg_value2': avg_value2,
        'avg_value3': avg_value3,
        'avg_value4': avg_value4,
    }



    return render(request, 'reviews_platform.html',context)