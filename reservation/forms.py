from .models import Reservation
from django import forms

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'number_of_persons', 'Date',)


