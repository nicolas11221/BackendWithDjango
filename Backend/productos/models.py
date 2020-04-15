from django.db import models


#Controladores

  # CharField  = Caracteres

  # max_length = Max De Caracteres
  # min_length = Min De Caracteres
  # max_digits = Max De Digitos

  # decimal_places = Numeros De Decimales
  # DecimalField   = Numeros Decimales
  # integerField   = Numeros Enteros
  # BooleanField   = Verdadero o Falso

  # DateTimeField(auto_now_add=True)     = La creacion de cualquer modelo, guarde fecha y hora exacta cuando se creo
  # models.DateTimeField(auto_now=True)  = Cada vez que se modifique cualquer registro saldra la fecha y hra exacta

class Chela(models.Model): 
    marca        = models.CharField(max_length=20)
    cant_alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    mililitros   = models.IntegerField()
    artesanal    = models.BooleanField()
    nacionalidad = models.CharField(max_length=50, blank=True)
    creado       = models.DateField(auto_now_add=True)
    editado      = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.marca
