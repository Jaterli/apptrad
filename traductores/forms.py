from django import forms
from traductores.models import Traductor, Combinacion, PerfilProfesional
from .constantes import SERVICIOS, SOFTWARES, SEXO, EXPERIENCIA, NIVEL_ESTUDIOS, PAISES, PROVINCIAS, IDIOMAS, SITUACIONES, TIPOS_TEXTO

class TraductorForm(forms.ModelForm):

    class Meta:
        model = Traductor
        fields = ['nombre','apellidos','direccion','cp','pais','provincia','f_nacimiento','sexo','tlf_mv','tlf_fijo','email']


class CombinacionForm(forms.ModelForm):

    servicios = forms.MultipleChoiceField(
        choices=SERVICIOS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-columns'}),  # Esto permite seleccionar múltiples valores con checkboxes
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(CombinacionForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.initial['servicios'] = list(self.instance.servicios.split(', '))

    def clean_servicios(self):
        return ', '.join(self.cleaned_data['servicios'])

    
class PerfilProfesionalForm(forms.ModelForm):
    lenguas_nativas = forms.MultipleChoiceField(
        choices=IDIOMAS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-columns'}),  
        required=False
    )

    textos = forms.MultipleChoiceField(
        choices=TIPOS_TEXTO,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-columns'}), 
        required=False
    )

    softwares = forms.MultipleChoiceField(
        choices=SOFTWARES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-columns'}), 
        required=False
    )    

    # class Meta:
    #     model = PerfilProfesional
    #     fields = ['traductor','lenguas_nativas', 'titulacion', 'experiencia', 'textos']

    def __init__(self, *args, **kwargs):
        super(PerfilProfesionalForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.initial['lenguas_nativas'] =  list(self.instance.lenguas_nativas.split(', '))
            self.initial['textos'] =  list(self.instance.textos.split(', '))
            self.initial['softwares'] =  list(self.instance.softwares.split(', '))


    def clean_lenguas_nativas(self):
        return ', '.join(self.cleaned_data['lenguas_nativas'])        
    def clean_textos(self):
        return ', '.join(self.cleaned_data['textos'])   
    def clean_softwares(self):
        return ', '.join(self.cleaned_data['softwares'])       