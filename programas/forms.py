from django import forms

class ProgramaForm(forms.Form):
    nombre = forms.CharField(error_messages = { 'required' : 'Debe ingresar un nombre'})
    descripcion = forms.CharField(error_messages = { 'required' : 'Debe ingresar un descripcion'})
    duracion = forms.CharField(error_messages = { 'required' : 'Debe ingresar una duracion'})
    costo = forms.CharField(error_messages = { 'required' : 'Debe ingresar un costo'})
    lugar = forms.CharField(error_messages = { 'required' : 'Debe ingresar un lugar'})
    lat = forms.CharField(error_messages = { 'required' : 'Debe seleccionar la ubicacion en un mapa'})
    lat = forms.CharField(error_messages = { 'required' : 'Debe seleccionar la ubicacion en un mapa'})
