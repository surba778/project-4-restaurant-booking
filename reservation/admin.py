from django.contrib import admin

# Register your models here.
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'email', 'number_of_persons', 'date', 'time')

admin.site.register(Reservation, ReservationAdmin)
