from django import forms
from .models import Top, Bottom, Match


class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields = ['image']


class BottomForm(forms.ModelForm):
    class Meta:
        model = Bottom
        fields = ['image']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['top', 'bottom']
    top = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)
    bottom = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['top'].queryset = Top.objects.filter(user=user)
        self.fields['bottom'].queryset = Bottom.objects.filter(user=user)