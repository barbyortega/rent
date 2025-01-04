from django.db import models
from django import forms

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)
    nombre = models.CharField(max_length=100)



    def __str__(self):
        return str(self.genero)

class Cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True) 


    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

class Auto(models.Model):
    marca             = models.CharField(primary_key=True, max_length=10)
    nombre            = models.CharField(max_length=20)
    color             = models.CharField(max_length=20)
    cant_pasajeros= models.CharField(max_length=20)
    annio             = models.DateField(blank=False, null=False) 
    id_auto           = models.CharField(max_length=20) 
    tipo_vehiculo     = models.CharField(max_length=45)
    combustible       = models.CharField(unique=True, max_length=100, blank=True, null=True)
    valor             = models.IntegerField( blank=True, null=True)  

class Reservas(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_reserva = models.DateField()
    mensaje = models.TextField(blank=True, null=True)
    tipo_vehiculo = models.CharField(max_length=50)

class ReservaForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre Completo', max_length=100)
    numero_telefono = forms.CharField(label='Número de Teléfono', max_length=15)
    lugar_retiro = forms.CharField(label='Lugar de Retiro', max_length=100)
    lugar_entrega = forms.CharField(label='Lugar de Entrega', max_length=100)
    fecha_retiro = forms.DateField(label='Fecha de Retiro', widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_entrega = forms.DateField(label='Fecha de Entrega', widget=forms.DateInput(attrs={'type': 'date'}))

    def __str__(self):  
        return str(self.marca)+" "+str(self.nombre) 
