from django.shortcuts import render
from menu.models import Menu

# Create your views here.
def menu(request):
    menu = Menu.objects.all()
    context = {
            'menu' : menu,       
    }
    return render(request, 'menu/menu.html', context)

    
        
   