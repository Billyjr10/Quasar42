from django.contrib import admin
from .models import Contact
from .models import Reservation

admin.site.register(Contact)
admin.site.register(Reservation)

