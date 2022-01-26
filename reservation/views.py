from django.template import context
from .models import Reservation
from django.shortcuts import render
from .forms import BookingTableForm

from reservation.models import Reservation

def home(request):
    return render(request, 'reservation/home.html', context)

def make_reservation(request):
    return render(request, 'reservation/book.html', context)

def book(request):
    reserve_form = BookingTableForm()

    if request.method == 'POST':
        reserve_form = BookingTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}
    return render(request, 'reservation/booked.html', context)

def bookings(request):
    user = request.user
    bookings = Reservation.objects.filter(user=user)
    context = {'bookings': bookings}
    return render(request, 'reservation/bookings.html', context)