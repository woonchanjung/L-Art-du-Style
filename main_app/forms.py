from django import forms
from .models import Top, Bottom


class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields = ['name', 'image']


class BottomForm(forms.ModelForm):
    class Meta:
        model = Bottom
        fields = ['name', 'image']

