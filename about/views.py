from django.shortcuts import render
from .models import About, We_Are_Feane
# Create your views here.


def about_list(request):
    about = About.objects.last()
    we_are_feane = We_Are_Feane.objects.all()

    context = {
        'about': about,
        'We_Are_Feane': We_Are_Feane,
    }

    return render(request, 'about/about.html', context)
