from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('',views.home, name='home'),
    path('book',views.book, name='book'),
    path('booked', views.booked, name='booked')
    
]