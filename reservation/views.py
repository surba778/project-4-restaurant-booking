from django.template import context
from .models import Reservation
from django.shortcuts import render
from .forms import BookingTableForm



from reservation.models import Reservation

def booking_table(request):
    
    context = {}
    return render(request , 'Reservation/reservation.html' , context )
