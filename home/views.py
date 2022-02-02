from django.shortcuts import render
from menu.models import Menu
from about.models import We_Are_Feane
# Create your views here.


def home(request):

    menu = Menu.objects.all()
    we_are_feane = We_Are_Feane.objects.all()

    context = {
        'menu': menu,
        'we_are_feane': we_are_feane,
    }

    return render(request, 'home/index.html', context)
