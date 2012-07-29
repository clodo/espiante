from models import Programa, Perfil
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput

class ProgramaForm(ModelForm):
    class Meta:
        model = Programa
        widgets = {
            'lon' : HiddenInput,
            'lat' : HiddenInput,
            'ranking' : HiddenInput,
        }



