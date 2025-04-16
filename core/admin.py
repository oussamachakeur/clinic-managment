from django.contrib import admin
from .models import CustomUser , Doctor , Patient , Receptionist ,Booking



admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Receptionist)
admin.site.register(Booking)