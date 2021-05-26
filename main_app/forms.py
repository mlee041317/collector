from django import forms
from .models import Moment, New

class MomentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = ('name', 'description', 'month', 'year')


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('date', 'people', 'feeling')