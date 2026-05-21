from django import forms
from season import models as m


class SeasonForm(forms.ModelForm):
    class Meta:
        model = m.Season
        fields = ['name', 'image_url']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = m.Chapter
        fields = ['number']


class DragaDataForm(forms.ModelForm):
    class Meta:
        model = m.DragaSeasonenData
        fields = ['draga', 'image_url']



