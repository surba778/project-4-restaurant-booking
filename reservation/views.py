from .models import Reservation
from django.shortcuts import render
from .forms import BookTableForm
from django.views import generic


from reservation.models import Reservation

def book_table(request):
    reserve_form = BookTableForm()

    if request.method == 'POST':
        reserve_form = BookTableForm(request.POST)

    if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}
    return render(request, 'reservation/book.html', context)

