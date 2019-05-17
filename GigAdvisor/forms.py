from django import forms
from django.forms import Textarea
from .models import Recensioni


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Recensioni
        fields = ['titolo', 'descrizione']
        widgets = {
            'titolo': Textarea(attrs={'cols': 60, 'rows': 1}),
            'descrizione': Textarea(attrs={'cols': 60, 'rows': 8}),

        }
