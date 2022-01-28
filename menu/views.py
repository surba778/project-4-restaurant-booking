from django.shortcuts import render
from menu.models import Menu

# Create your views here.
    def home(request):
    menu = Menu.objects.all()
    context = {
        'menu' : menu,       
    }
    return render(request, 'menu/menu.html', context)

    
        
   