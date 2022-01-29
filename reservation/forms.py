from .models import Reservation
from django import forms

class BookTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'number_of_persons',)


