from django.contrib import admin
from traductores.forms import PerfilProfesionalForm, TraductorForm, CombinacionForm
from .models import Traductor, Combinacion, Acceso, PerfilProfesional, Consulta
from .constantes import SERVICIOS, SOFTWARES, SEXO, EXPERIENCIA, NIVEL_ESTUDIOS, PAISES, PROVINCIAS, IDIOMAS, SITUACIONES, TIPOS_TEXTO

# Register your models here.
admin.site.register(Acceso)
admin.site.register(Consulta)


@admin.register(Traductor)
class TraductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')
    form = TraductorForm  # Aquí vinculamos el formulario personalizado con el admin
    
    class Media:
        css = {
            'all': ('css/admin_custom.css',) 
        }


@admin.register(Combinacion)
class CombinacionAdmin(admin.ModelAdmin):
    list_display = ('traductor', 'origen', 'destino', 'servicios')
    form = CombinacionForm  # Aquí vinculamos el formulario personalizado con el admin
    
    class Media:
        css = {
            'all': ('css/admin_custom.css',) 
        }


@admin.register(PerfilProfesional)
class PerfilProfesionalAdmin(admin.ModelAdmin):
    list_display = ('traductor','lenguas_nativas', 'titulacion', 'experiencia', 'textos')
    form = PerfilProfesionalForm  # Aquí vinculamos el formulario personalizado con el admin
    
    class Media:
        css = {
            'all': ('css/admin_custom.css',) 
        }
