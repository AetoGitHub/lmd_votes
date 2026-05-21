from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'texto']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-nombre',
                'placeholder': 'Tu nombre',
            }),
            'texto': forms.Textarea(attrs={
                'class': 'input-texto',
                'rows': 4,
                'placeholder': 'Escribe tu mensaje...',
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre.lower() == 'letal':
            raise forms.ValidationError('El nombre "letal" no está permitido.')
        return nombre
