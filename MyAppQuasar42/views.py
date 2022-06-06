from ast import Return
import datetime
import random
from re import template

from unittest import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import MBNewUserForm, ReservationForm2,  ReservationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import ContactForm

from django.contrib import messages

from django.utils.dateparse import parse_date
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
      form = ContactForm
      if request.method == 'POST':
          contactForm=ContactForm(request.POST)
          if contactForm.is_valid():
              contactForm.save()
              messages.success(request,'Message envoyé avec succes!!!!!')
              return redirect('/contact')
      return render(request, 'contact.html', {'form':form})





def signup(request):
   
	
	form = MBNewUserForm()
	if request.method == 'POST':
		form = MBNewUserForm(request.POST)
		if form.is_valid():
			username = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Compte créé pour ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'signup.html', context)



def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logOut(request):
    logout(request)
    return redirect('login')



def randomOrderNumber(length):
    sample  = 'ABCDEFGH0123456789'
    number0 = ''.join((random.choice(sample) for i in range (length)))
    return number0


def defaultconverterDate(o):
  if isinstance(o, datetime.date):
      return o.__str__()




@login_required(login_url='/login')
def reservation (request):
     form = ReservationForm()
     if request.method == 'POST':
          reservationForm=ReservationForm(request.POST)
          if reservationForm.is_valid():
              data = reservationForm.cleaned_data
              request.session['Name'] = data['Name']
              request.session['Phone'] = data['Phone']
              request.session['Email'] = data['Email']
              request.session['Date_Choisie'] =  json.dumps(data['Date_choisie'].isoformat())
              request.session['Heure_Choisie'] = json.dumps(data['Heure_choisie'].isoformat())
              reservation=reservationForm.save()
              reservation.ref=randomOrderNumber(6)
              reservation.save()
              messages.success(request, f'Votre réservation est enregistrée (ref {reservation.ref})' )
              return redirect('/reservation' ) 
          else:
                messages.success(request,'Votre réservation n`\'est pas valide !!!!!')
                return redirect('/reservation') 
     return render(request, 'reservation.html', {'form':form})







def about(request):
    return render(request, 'about.html')



def success(request):
       return render(request,'success.html', {'randomnum':request.session['ref']})

def base(request):
    return render(request, 'base.html')       
   
    
