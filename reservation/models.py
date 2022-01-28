from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.

class Reservation(models.Model):

    class Meta:
        unique_together = [['table', 'date']]
        
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    table = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.name
