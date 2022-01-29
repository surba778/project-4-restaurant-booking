from django.urls import path
from . import views

urlpatterns = [
    
    path('reservation',views.make_reservation, name='reservation'),
]