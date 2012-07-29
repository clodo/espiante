from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from programas.models import Programa, Perfil
from forms import ProgramaForm

def home(request):
    perfiles = Perfil.objects.all()
    programas_destacados = Programa.objects.order_by('-ranking')[:4]
    return render_to_response('home.html',
                            { 'perfiles': perfiles,
                            'programas_destacados': programas_destacados },
                            context_instance = RequestContext(request))

def ver_programa(request, programa_id):
    programa = Programa.objects.get(pk=programa_id)
    return render_to_response('programa.html', 
                              { 'programa': programa },
                              context_instance = RequestContext(request))

def redactar(request, programa_id=None):
    template = 'redactar.html'
    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data
            return HttpResponseRedirect('/gracias/')
    else:
        form = ProgramaForm()

    return render_to_response(template, { 'form' : form }, context_instance = RequestContext(request))

def redactar_gracias(request):
    return render_to_response('redactar_gracias.html', context_instance = RequestContext(request))

class ProgramasListView(ListView):
    context_object_name = "programas"
    #queryset = Programa.objects.order_by('-ranking')
    template_name = "programas.html"

    def get_queryset(self):
        perfil_slug = self.kwargs['perfil']
        lugar = self.kwargs['lugar']

        return Programa.objects.filter(perfil__slug=perfil_slug)


    #def get_context_data(self, **kwargs):
    #    context = super(ProgramasListView, self).get_context_data(**kwargs)
    #    context['lugar'] = Marca.objects.all()
    #    context['perfil'] = Marca.objects.all()
    #    return context
