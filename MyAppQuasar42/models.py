import email
from email import message
from pyexpat import model

from unittest.util import _MAX_LENGTH
from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 25)
    email = models.EmailField(max_length= 30)
    phone = models.IntegerField(max_length=10)
    message = models.TextField(blank=True)






class Reservation(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField(max_length=10)
    Email = models.EmailField(max_length=40)
    Date_choisie = models.DateField(null = True)
    Heure_choisie = models.TimeField(null = True)