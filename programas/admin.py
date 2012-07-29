from django.contrib import admin
from models import Perfil, Guia, Programa, ImagenPrograma

class PerfilAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

class ImagenProgramaInline(admin.TabularInline):
    model = ImagenPrograma

class ProgramaAdmin(admin.ModelAdmin):
    inlines = (ImagenProgramaInline, )

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Guia)
admin.site.register(Programa, ProgramaAdmin)
