from django import forms
from django.db import models
from django.forms import Textarea
from .models import Recensioni
from .models import Profile



class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['titolo'].required = True




    class Meta:
        model = Recensioni
        fields = ['titolo', 'descrizione']
        fields_required = ['titolo', 'descrizione']
        widgets = {
            'titolo': Textarea(attrs={'cols': 60, 'rows': 1}),
            'descrizione': Textarea(attrs={'cols': 60, 'rows': 8}),
        }

CHOICES = [
    ('M', 'Maschile'),
    ('F', 'Femminile'),
]
YEARS= [x for x in range(1940,2021)]

class ProfileForm(forms.ModelForm):
    sesso = forms.ChoiceField(required=True, choices=CHOICES)
    birth_date= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model = Profile
        fields = ('nome', 'cognome', 'residenza','sesso', 'birth_date', 'titolo_di_studio','avatar')
        widgets = {
            'avatar' : forms.FileInput(attrs={'class': 'form-control','id' : 'input-file'}),
            }
        labels = {
            'nome': ('Name'),
            'cognome': ('Surname'),
            'avatar': ('Photo'),

        }
