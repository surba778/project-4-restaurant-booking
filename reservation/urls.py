from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('',views.book_table, name='book_table'),
]