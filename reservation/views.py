from django.template import context
from .models import Reservation
from django.shortcuts import render
from .forms import BookingTableForm

from reservation.models import Reservation

def book_table(request):
    reserve_form = BookingTableForm()

    if request.method == 'POST' :
        reserve_form = BookingTableForm(request.POST)
        
        if reserve_form.is_valid():
            reserve_form.save()


    context = {'form' : reserve_form}
    return render(request , 'Reservation/book.html' , context )
