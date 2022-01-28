from django.template import context
from .models import Reservation
from django.shortcuts import render
from .forms import ReserveTableForm

from reservation.models import Reservation

def home(request):
    return render(request, 'reservation/home.html', context)

def make_reservation(request):
    return render(request, 'reservation/book.html', context)

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}
    return render(request, 'Reservation/book.html', context)

def booked(request):
    user = request.user
    booked = Reservation.objects.filter(user=user)
    context = {'booked': book}
    return render(request, 'reservation/booked.html', context)