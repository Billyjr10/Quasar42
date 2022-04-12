from ast import Return
import random
from re import template
from unittest import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import MBNewUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import ContactForm
from .forms import ReservationForm
from django.contrib import messages


  

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def contact(request):
      form = ContactForm
      if request.method == 'POST':
          contactForm=ContactForm(request.POST)
          if contactForm.is_valid():
              contactForm.save()
              messages.success(request,'Message envoyé avec succes!')
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

		user = authenticate(request, username=username, password=password)

		if user is not None:
			
			return render(request ,'index.html')
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



@login_required(login_url='/login')
def reservation (request):
     form = ReservationForm
     if request.method == 'POST':
          reservationForm=ReservationForm(request.POST)
          if reservationForm.is_valid():
              reservationForm.save()
              
              messages.success(request,'Votre réservation a bien été enregistré !')
                      
              return redirect('/reservation') 
     return render(request, 'reservation.html', {'form':form})



def about(request):
    return render(request, 'about.html')