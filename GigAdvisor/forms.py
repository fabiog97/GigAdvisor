from django import forms

from .models import Recensioni


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Recensioni
        fields = ('titolo','descrizione')
