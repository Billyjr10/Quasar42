from ast import Return
import random
from re import template
from unittest import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import NewUserForm
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
    ctx = {'reservation': Reservation.objects.all()}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'templates/signup.html', ctx)

def logIn(request):
    if request.POST:
        username =  request.POST.get('username')
        pwd =  request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Les champs sont incorects')
    ctx = {'reservation': Reservation.objects.all(), 'active_link': 'login'}
    return render(request, 'templates/login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')



def randomOrderNumber(length):
    sample  = 'ABCDEFGH0123456789'
    number0 = ''.join((random.choice(sample) for i in range (length)))
    return number0



@login_required
def reservation (request):
     form = ReservationForm
     if request.method == 'POST':
          reservationForm=ReservationForm(request.POST)
          if reservationForm.is_valid():
              reservationForm.save()
              
              messages.success(request,'Votre réservation a bien été enregistré !')
                      
              return redirect('/reservation') 
     return render(request, 'reservation.html', {'form':form})


    