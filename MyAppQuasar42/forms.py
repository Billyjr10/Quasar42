from dataclasses import fields
from os import rename
from pyexpat import model
from django.forms import ModelForm
from .models import MBContact, MBReservation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    class Meta :
        model = MBContact
        fields = '__all__'




class MBNewUserForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MBUserForm(User):
    model = User 
    fields = '__all__' 



class ReservationForm(ModelForm):
    class Meta :
        model = MBReservation
        fields = '__all__'     