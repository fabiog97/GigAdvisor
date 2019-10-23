from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from static.fusioncharts import FusionCharts
from static.fusioncharts import FusionTable
from static.fusioncharts import TimeSeries
from collections import OrderedDict
from django.shortcuts import render
from GigAdvisor.forms import ReviewForm
from GigAdvisor.forms import ProfileForm
from .models import *
from datetime import datetime
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from decimal import Decimal
import simplejson
import requests
import json
import pytz


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def profiloView(request):
    context = {'profile_page': "active"}  # new info here
    #recensioni = Recensioni.objects.filter(platform__id=platform.id).values()
    return render(request, 'profile.html',context)


def createProfile(request):

    if request.method == 'POST':
        if(request.user.is_authenticated):
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            #form_nome = profile_form.nome
            
            if profile_form.is_valid():
                profile_form.modified = False
                profile_form.save()
                return render(request, 'success_newprofile.html')
            else:
                return render(request, 'unsuccess_review.html')
    else:
        profile_form = ProfileForm(request.POST)
        return render(request, 'profile_form.html', {'form': profile_form})


def updateProfile(request):
    context = {'profile_page': "active"}  # new info here
    if request.method == 'POST':
        if(request.user.is_authenticated):
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if profile_form.is_valid():
                
                profile_form.save()
                return render(request, 'profile.html', context)
            else:
                return render(request, 'unsuccess_review.html')
    else:
        
        p = Profile.objects.filter(user=request.user)[:1].get()
        
        
        
        profile_form = ProfileForm(initial={'avatar': p.avatar,'nome':  p.nome, 'cognome':  p.cognome, 'residenza': p.residenza, 'titolo_di_studio': p.titolo_di_studio, 'sesso': p.sesso, 'birth_date':p.birth_date})
        profile_form.modified = True
        return render(request, 'profile_form.html', {'form': profile_form})
    

def charts(request):

    dataSource = {}
    dataSource['chart'] = {
        "caption": "",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "baseFontSize": "14",
            "xAxisNamePadding": "30",
            "yAxisNamePadding": "30",
            "chartLeftMargin": "70",
            "chartTopMargin": "70",
            "chartRightMargin": "70",
            "chartBottomMargin": "70",
             "usePlotGradientColor": "1",
        "usePlotGradientColor": "1",
        "plotGradientColor":"#ffffff"
        }
    dataSource['data'] = []

    for key in Platform.objects.all():
      data = {}
      
      data['label'] = key.nome
      data['value'] = simplejson.dumps(key.rating, use_decimal=True)
      dataSource['data'].append(data)


    dataSource1 = {}
    dataSource1['chart'] = {
        "caption": "",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "5d62b5,29c3be,f2726f",
            "baseFontSize": "12",
            "chartLeftMargin": "30",
            "chartTopMargin": "50",
            "chartRightMargin": "30",
            "chartBottomMargin": "50",
            "xAxisNamePadding": "30",
            "yAxisNamePadding": "30",
        }
    dataSource1['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value1 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value1')).get('value1__avg')
        
        data['label'] = plat.nome
        if(avg_value1  is None):
             data['value'] = 0
        else:
            data['value'] = int(avg_value1)
        dataSource1['data'].append(data)
        avg_value1 = 0
        
    dataSource2 = {}
    dataSource2['chart'] = {
        "caption": "",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "5d62b5,29c3be,f2726f",
            "baseFontSize": "12",
            "chartLeftMargin": "30",
            "chartTopMargin": "50",
            "chartRightMargin": "30",
            "chartBottomMargin": "50",
            "xAxisNamePadding": "30",
            "yAxisNamePadding": "30",
        }
    dataSource2['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value2 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value2')).get('value2__avg')
        data['label'] = plat.nome
        if(avg_value2 is None):
             data['value'] = 0
        else:
            data['value'] = int(avg_value2)
        dataSource2['data'].append(data)

    dataSource3 = {}
    dataSource3['chart'] = {
        "caption": "",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "5d62b5,29c3be,f2726f",
            "baseFontSize": "12",
            "chartLeftMargin": "30",
            "chartTopMargin": "50",
            "chartRightMargin": "30",
            "chartBottomMargin": "50",
            "xAxisNamePadding": "30",
            "yAxisNamePadding": "30",
        }
    dataSource3['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value3 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value3')).get('value3__avg')
        data['label'] = plat.nome
        if(avg_value3 is None):
             data['value'] = 0
        else:
            data['value'] = int(avg_value3)
        dataSource3['data'].append(data)

    dataSource4 = {}
    dataSource4['chart'] = {
        "caption": "",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "5d62b5,29c3be,f2726f",
            "baseFontSize": "12",
            "chartLeftMargin": "30",
            "chartTopMargin": "50",
            "chartRightMargin": "30",
            "chartBottomMargin": "50",
            "xAxisNamePadding": "30",
            "yAxisNamePadding": "30",
        }
    dataSource4['data'] = []

    for plat in Platform.objects.all():
        data = {}
        avg_value4 = Recensioni.objects.filter(platform__id=plat.id).aggregate(Avg('value4')).get('value4__avg')
        data['label'] = plat.nome
        if(avg_value4 is None):
             data['value'] = 0
        else:
            data['value'] = int(avg_value4)
        dataSource4['data'].append(data)



    column2D = FusionCharts("column2d", "myFirstChart", "100%", "400", "chart-container", "json", dataSource)

    graph1 = FusionCharts("column2d", "myFirstChart1", "100%", "300", "chart1-container", "json", dataSource1)
    graph2 = FusionCharts("column2d", "myFirstChart2", "100%", "300", "chart2-container", "json", dataSource2)
    graph3 = FusionCharts("column2d", "myFirstChart3", "100%", "300", "chart3-container", "json", dataSource3)
    graph4 = FusionCharts("column2d", "myFirstChart4", "100%", "300", "chart4-container", "json", dataSource4)
        
    return render(request, 'charts.html', {'output': column2D.render(), 'output1': graph1.render(), 'output2': graph2.render(), 'output3': graph3.render(), 'output4': graph4.render(), 'charts_page': "active"})

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
        context = {
            'platform_page':'active',
        }
        if form.is_valid():
            titolo = form.cleaned_data['titolo']
            descrizione = form.cleaned_data['descrizione']
            range1 = int(request.POST['range1'])
            range2 = int(request.POST['range2'])
            range3 = int(request.POST['range3'])
            range4 = int(request.POST['range4'])
            luogo = request.POST['luogo']
            
            
            platform = Platform.objects.get(id=id)

            r = Recensioni(titolo=titolo, descrizione=descrizione,platform=platform, value1=range1, value2=range2, value3=range3, value4=range4, luogo = luogo)
            r.save()
            value1_avg = Recensioni.objects.filter(platform__id=id).aggregate(Avg('value1')).get('value1__avg')
            value2_avg = Recensioni.objects.filter(platform__id=id).aggregate(Avg('value2')).get('value2__avg')
            value3_avg = Recensioni.objects.filter(platform__id=id).aggregate(Avg('value3')).get('value3__avg')
            value4_avg = Recensioni.objects.filter(platform__id=id).aggregate(Avg('value4')).get('value4__avg')

            platform.rating = (value1_avg + value2_avg + value3_avg + value4_avg)/4
            platform.save()
            

            return render(request, 'success_review.html',context)
        else:
            return render(request, 'unsuccess_review.html',context)
    else:
        form = ReviewForm(request.POST)
        context = {
        'form': form,
        'platform_page':'active',
        }
        return render(request, 'reviews_form.html', context)

def success(request):
    context = {
        'platform_page':'active',
        }
    return render(request, 'platforms.html',context )



def andamento_platform (request, id):

    platform = Platform.objects.get(id=id)
    
    recensioni = Recensioni.objects.filter(platform__id=platform.id).values()
    avg_value1 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value1'))
    avg_value2 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value2'))
    avg_value3 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value3'))
    avg_value4 = Recensioni.objects.filter(platform__id=platform.id).aggregate(Avg('value4'))

    schema_chart = [{
        "name": "Time",
        "type": "date",
        "format": "%d-%b-%y"
        }, {
        "name": "Type",
        "type": "string"
        }, {
        "name": "Rating Value",
        "type": "number"
        }]
    funds = Recensioni.objects.filter(platform__id=id).all()
    data = serializers.serialize("json", funds, fields=('data','value1','value2','value3', 'value4',))
    
    y = json.loads(data)
    
    final_data = []
    
    
    for i in range(len(y)):
        z = y[i]
        data = datetime.strptime(z['fields']['data'], '%Y-%m-%dT%H:%M:%S.%f%z')
        data = data.strftime("%d-%b-%y")
        d1 = [data, "Safety at work", z['fields']['value1']]
        d2 = [data, "Contracts transparency", z['fields']['value2']]
        d3 = [data, "Payment timeliness", z['fields']['value3']]
        d4 = [data, "Platform's fairness", z['fields']['value4']]
        final_data.append(d1)
        final_data.append(d2)
        final_data.append(d3)
        final_data.append(d4)

    fusionTable = FusionTable(str(schema_chart), str(final_data))
    
    timeSeries = TimeSeries(fusionTable)

    """
    dataSource4['chart'] = {
        "caption": "",
            "xAxisName": "Platforms",
            "yAxisName": "Values",
            "numberPrefix": "",
            "theme": "zune",
            "paletteColors": "5d62b5,29c3be,f2726f",
            "baseFontSize": "12",
            "chartLeftMargin": "30",
            "chartTopMargin": "50",
            "chartRightMargin": "30",
            "chartBottomMargin": "50",
            "xAxisNamePadding": "30",
            "yAxisNamePadding": "30",
        }
    """

    
    timeSeries.AddAttribute('chart', '{"paletteColors": "#28a745,#dc3545,#ffc107,#17a2b8"}')
    timeSeries.AddAttribute('caption', '{"text":"Platform’s rating trends"}')
    timeSeries.AddAttribute('chartTopMargin', '{"chartTopMargin":"300"}')
    timeSeries.AddAttribute('subcaption', '{"text":""}')
    timeSeries.AddAttribute('series', '"Type"')
    #timeSeries.AddAttribute('xaxis', '[{"plot":"Rating Value","title":"Sale Value","format":{"prefix":""}}]')
    
    dataSource5 = OrderedDict()

    # The `mapConfig` dict contains key - value pairs data
    # for chart attribute
    mapConfig = OrderedDict()
    mapConfig["animation"] = "0"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#ffffff"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    mapConfig["caption"] = "Rating map"
    mapConfig["chartTopMargin"] = "30"
    mapConfig["captionHorizontalPadding"] = "70"
    mapConfig["captionAlignment"] = "left"
    mapConfig["captionFontSize"] = "16"
    mapConfig["subcaptionFontSize"] = "12"
    mapConfig["captionFontBold"] = "1"
    mapConfig["captionFontColor"] = "#5F5F5F"
    mapConfig["subcaptionFontColor"] = "#B1B1B1"
    mapConfig["connectorcolor"]= "000000"
    mapConfig["fillalpha"]= "80"
    mapConfig["hovercolor"]= "CCCCCC"
    mapConfig["theme"] = "zune"

    # Map color range data
    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "0.0",
            "maxValue": "1.0",
            "code": "#FFD74D"
        }, {
            "minValue": "1.0",
            "maxValue": "2.0",
            "code": "#FB8C00"
        }, {
            "minValue": "2.0",
            "maxValue": "3.0",
            "code": "#E65100"
        },{
            "minValue": "3.0",
            "maxValue": "4.0",
            "code": "#e03400"
        },{
            "minValue": "4.0",
            "maxValue": "5.0",
            "code": "#e00400"
        }]
    }

  

    dataSource5["chart"] = mapConfig
    dataSource5["colorrange"] = colorDataObj
    dataSource5["data"] = []
    
    
    avg = 0
    for r in Recensioni.objects.filter(platform__id=id):
        
        avg__luogo_value1 = Recensioni.objects.filter(platform__id=id, luogo = r.luogo).aggregate(Avg('value1')).get('value1__avg')
        avg__luogo_value2 = Recensioni.objects.filter(platform__id=id, luogo = r.luogo).aggregate(Avg('value2')).get('value2__avg')
        avg__luogo_value3 = Recensioni.objects.filter(platform__id=id, luogo = r.luogo).aggregate(Avg('value3')).get('value3__avg')
        avg__luogo_value4 = Recensioni.objects.filter(platform__id=id, luogo = r.luogo).aggregate(Avg('value4')).get('value4__avg')
        avg = (avg__luogo_value1+avg__luogo_value2+avg__luogo_value3+avg__luogo_value4)/4
        
        
        dataSource5["data"].append({
            "id": r.luogo,
            "value": str(avg),
            "showLabel": 1
        })
    


    # Iterate through the data in `mapDataArray` and insert in to the `dataSource["data"]` list.
    #The data for the `data` should be in an array wherein each element
    #of the array is a JSON object# having the `id`, `value` and `showlabel` as keys.
    #for i in range(len(mapDataArray)):
    #    dataSource5["data"].append({
    #        "id": mapDataArray[i][0],
    #       "value": mapDataArray[i][1],
    #       "showLabel": mapDataArray[i][2]
    #    })

    # Create an object for the world map using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    fusionMap = FusionCharts("maps/italy", "myFirstMap", "100%", "500", "myFirstmap-container", "json", dataSource5)


    fcChart = FusionCharts("timeseries", "ex1", "100%", "450", "chart-1", "json", timeSeries)

    context = {
        'platform': platform,
        'recensioni': recensioni,
        'avg_value1': avg_value1,
        'avg_value2': avg_value2,
        'avg_value3': avg_value3,
        'avg_value4': avg_value4,
        'output5': fcChart.render(),
        'output6': fusionMap.render(),
        'platform_page':'active',
    }
   

    return render(request, 'andamento_platform.html', context)


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
        'platform_page':'active',
    }



    return render(request, 'reviews_platform.html',context)