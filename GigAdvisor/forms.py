from django import forms
from django.forms import Textarea
from .models import Recensioni


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
