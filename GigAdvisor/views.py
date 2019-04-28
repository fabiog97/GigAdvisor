import datetime

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from datetime import datetime
from GigAdvisor.forms import ReviewForm
from .models import *

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class PlatformListView(generic.ListView):
    model = Platform

    context_object_name = 'platforms_list'
    queryset = Platform.objects.all()
    template_name = 'platforms.html'  # Specify your own template name/location



def recensione_new(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #r = form.save()
            titolo = form.cleaned_data['titolo']
            descrizione = form.cleaned_data['descrizione']

            r = Recensioni(titolo=titolo, descrizione=descrizione,platform=1)
            r.save()
            # redirect to a new URL: return HttpResponseRedirect('/success/')
            print('Success')
    else:
        form = ReviewForm(request.POST)
        return render(request, 'reviews_form.html', {'form': form})