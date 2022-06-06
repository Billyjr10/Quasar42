from asyncio.windows_events import NULL
import email
from email import message
from logging import PlaceHolder
from pyexpat import model
from tkinter import CASCADE

from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, HiddenInput, SplitDateTimeWidget, SplitHiddenDateTimeWidget



# Create your models here.
class MBContact(models.Model):
    name = models.CharField(max_length= 25)
    email = models.EmailField(max_length= 30)
    phone = models.IntegerField()
    message = models.TextField(blank=True)


CHOICES = (
        ('TR1', 'Terrain1'),
        ('TR2', 'Terrain2'),
        ('TR3', 'Terrain3'),
        ('BSK1', 'Basket1'),
        ('BSK2', 'Basket2'),
        ('BSK3', 'Basket3'),
        ('BX1', 'Boxe1'),
        ('BX2', 'Boxe2'),
        ('BX3', 'Boxe3'),
    )  

class MBLieux(models.Model):
    Nom_du_lieu_choisie  = models.CharField(max_length=50,   default='Terrain1')
    def __str__(self):
        return self.Nom_du_lieu_choisie

class MBReservation(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=40)
    Nom_du_lieu_choisie = models.ForeignKey(to='MBLieux',  on_delete=models.CASCADE, )
    Date_choisie = models.DateField(blank=False)
    Heure_choisie = models.TimeField(blank=False)
    ref = models.CharField(max_length=6)










    
  

    

