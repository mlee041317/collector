from django import forms
from .models import Moment, Many

class MomentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = ('name', 'description', 'month', 'year')


class ManyForm(forms.ModelForm):
    class Meta:
        model = Many
        fields = ('date', 'people', 'feeling')