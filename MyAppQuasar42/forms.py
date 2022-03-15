from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Contact, Reservation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class ContactForm(ModelForm):
    class Meta :
        model = Contact
        fields = '__all__'




class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Inform a valid email adress')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReservationForm(ModelForm):
    class Meta :
        model = Reservation
        fields = '__all__'     