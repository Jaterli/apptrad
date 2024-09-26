from audioop import reverse
from django.db import models
from .constantes import SOFTWARES, SERVICIOS, SEXO, EXPERIENCIA, NIVEL_ESTUDIOS, PAISES, PROVINCIAS, IDIOMAS, SITUACIONES, TIPOS_TEXTO

# Create your models here.

class Traductor(models.Model):
    traductor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    cp = models.IntegerField()
    pais = models.CharField(max_length=50, choices=PAISES)
    provincia = models.CharField(max_length=50, choices=PROVINCIAS, null=True, blank=True)
    f_nacimiento = models.DateField()
    sexo = models.CharField(max_length=9, choices=SEXO)
    tlf_mv = models.CharField(max_length=18, null=True, blank=True)
    tlf_fijo = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(unique=True)    
    f_alta = models.DateTimeField(auto_now_add=True)
    f_acceso = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular del modelo.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    

class PerfilProfesional(models.Model):
    traductor = models.OneToOneField(Traductor, on_delete=models.CASCADE, related_name="perfil_profesional")
    lenguas_nativas = models.CharField(max_length=100, null=True, blank=True)
    estudios = models.CharField(max_length=40, choices=NIVEL_ESTUDIOS, null=True, blank=True)
    titulacion = models.CharField(max_length=50, null=True, blank=True)
    situacion = models.CharField(max_length=20, choices=SITUACIONES, null=True, blank=True)
    experiencia = models.CharField(max_length=20, choices=EXPERIENCIA, null=True, blank=True)
    textos = models.TextField(max_length=100, null=True, blank=True)
    softwares = models.TextField(max_length=250, null=True, blank=True, help_text="Seleccione los softwares que utiliza")

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular del modelo.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"Perfil profesional de {self.traductor.nombre}"


class Acceso(models.Model):
    traductor = models.OneToOneField(Traductor, on_delete=models.CASCADE, related_name="acceso")
    password = models.CharField(max_length=128) # hash

    def __str__(self):
        return f"Acceso de {self.traductor.nombre}" 


class Combinacion(models.Model):
    traductor = models.ForeignKey(Traductor, on_delete=models.CASCADE, related_name="combinaciones")
    origen = models.CharField(max_length=20, choices=IDIOMAS, null=True, blank=True)
    destino = models.CharField(max_length=20, choices=IDIOMAS, null=True, blank=True)
    servicios = models.CharField(max_length=100)
    tarifa_palabra = models.FloatField(default=0, blank=True)
    tarifa_jurada = models.FloatField(default=0, blank=True)
    tarifa_hora = models.FloatField(default=0, blank=True)

    def set_multiple_choice_list(self, field_value):
        self.field_value = ",".join(field_value)
    
    def get_multiple_choice_list(self):
        return self.servicios.split(",") if self.servicios else []
   
    def __str__(self):
        return f"{self.origen} -> {self.destino}. {self.traductor.nombre} {self.traductor.apellidos} ({self.traductor.email})"
    


class Consulta(models.Model):
    consulta_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True, default='')
    campos = models.TextField()
    operadores1 = models.CharField(max_length=100, default='')
    cadenas = models.CharField(max_length=200, default='')
    operadores2 = models.CharField(max_length=50, default='')
    consulta_sql = models.TextField()

    def __str__(self):
        return f"Consulta: {self.nombre}"    