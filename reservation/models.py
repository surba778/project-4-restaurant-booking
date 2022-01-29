from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.name
