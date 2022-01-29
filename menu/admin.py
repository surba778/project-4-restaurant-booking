from django.contrib import admin

from .models import Menu

class MenuAdmin(admin.ModelAdmin):  # instead of ModelAdmin
   
    list_display = ['name' ,'preperation_time', 'people', 'price']
    search_fields = ['name', 'description' ]

admin.site.register(Menu , MenuAdmin)
