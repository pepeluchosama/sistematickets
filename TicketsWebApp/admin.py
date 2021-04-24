from django.contrib import admin
from .models import Ticket
from django.contrib import messages
from django.utils.translation import ngettext

# Acciones




# Register your models here.

class Ticket_Admin(admin.ModelAdmin):
    list_display=("id","asunto","descripcion","solucionado")
    date_hierarchy="fecha"
    actions=['solucionar', 'no_solucionado']
    
    
    @admin.action(description='Marcar solucionado')
    def solucionar(self, request, queryset):
        updated=queryset.update(solucionado=True)
        self.message_user(request, ngettext(
            '%d ticket fue marcado como solucionado.',
            '%d tickets fueron marcados como solucionado.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Marcar NO solucionado')
    def no_solucionado(self, request, queryset):
        updated=queryset.update(solucionado=False)
        self.message_user(request, ngettext(
            '%d ticket fue marcado como NO solucionado.',
            '%d tickets fueron marcados como NO solucionado.',
            updated,
        ) % updated, messages.SUCCESS)

     

    

admin.site.register(Ticket, Ticket_Admin)