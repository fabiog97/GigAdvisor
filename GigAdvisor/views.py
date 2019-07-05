import datetime
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from datetime import datetime
from GigAdvisor.forms import ReviewForm
from .models import *
from django.http import HttpResponseRedirect

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def team(request):
    context = {'team_page': "active"}  # new info here
    return render(request, 'team.html', context)

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

            platform = Platform.objects.get(id=id)
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