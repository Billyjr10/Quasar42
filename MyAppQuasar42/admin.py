from django.contrib import admin
from .models import MBContact
from .models import MBReservation
from .models import MBLieux


admin.site.register(MBContact)
admin.site.register(MBReservation)
admin.site.register(MBLieux)

