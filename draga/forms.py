from django import forms
from .models import Feminosa


class FeminosForm(forms.ModelForm):
    class Meta:
        model = Feminosa
        fields = ['name', 'image']
