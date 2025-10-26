from django import forms
from .models import Faena

class FaenaForm(forms.ModelForm):
    class Meta:
        model = Faena
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'predio', 'operario_asignado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise forms.ValidationError('La fecha fin no puede ser anterior a la fecha de inicio.')
        return cleaned_data
