import datetime

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


class PlatformListView(generic.ListView):
    model = Platform

    context_object_name = 'platforms_list'
    queryset = Platform.objects.all()
    template_name = 'platforms.html'  # Specify your own template name/location



def recensione_new(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #r = form.save()
            titolo = form.cleaned_data['titolo']
            descrizione = form.cleaned_data['descrizione']
            platform = Platform.objects.get(id=id)
            r = Recensioni(titolo=titolo, descrizione=descrizione,platform=platform)
            r.save()

            return render(request, 'success_review.html')

    else:
        form = ReviewForm(request.POST)
        return render(request, 'reviews_form.html', {'form': form})

def success(request):
    return render(request, 'platforms.html')



def recensione_platform (request, id):
    platform_id = Platform.objects.get(id=id)
    context = {
        'nome': platform_id.nome,
        'categoria': platform_id.categoria,
        'photo': platform_id.photo,
    }

    recensioni = Recensioni.objects.filter(platform=platform_id)
    #passare la variabile 'recensioni' al metodo render
    return render(request, 'reviews_platform.html',context)