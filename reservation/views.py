from .models import Reservation
from django.shortcuts import render
from .forms import BookTableForm
from django.views import generic

from reservation.models import Reservation

def make_reservation(request):
    return render(request, 'reservation/book.html',)

def book_table(request):
    reserve_form = BookTableForm()

    if request.method == 'POST':
        reserve_form = BookTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}
    return render(request, 'Reservation/book.html', context)

def booked(request):
    user = request.user
    booked = Reservation.objects.filter(user=user)
    context = {'booked': book}
    return render(request, 'reservation/booked.html', context)