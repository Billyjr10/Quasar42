import email
from email import message
from logging import PlaceHolder
from pyexpat import model



from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import SplitDateTimeWidget, SplitHiddenDateTimeWidget



# Create your models here.
class MBContact(models.Model):
    name = models.CharField(max_length= 25)
    email = models.EmailField(max_length= 30)
    phone = models.IntegerField(max_length=10)
    message = models.TextField(blank=True)






class MBReservation(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField(max_length=10)
    Email = models.EmailField(max_length=40)
    Nom_du_lieu_choisie = models.TextField(blank=True)
    Date_choisie = models.TimeField(null = True)
    Heure_choisie = models.TimeField(null = True)