from django.utils.html import format_html
from django.contrib import admin

#from admin_auto_filters.filters import AutocompleteFilter
# Register your models here.
# Register your models here.
from .models import Datos_Baja


# Register your models here.
class AsignacionDeEquipoAdmin(admin.ModelAdmin):

    search_fields = ['Folio','status_baja__status_baja','Oficio','ticket_baja__ticket_baja',]
    list_display = ('Folio','fecha_de_baja','status_baja','Oficio','ticket_baja','asignacion_de_equipos','diagnostico',) 
    list_filter= ('status_baja','Oficio','periodo','ticket_baja','fecha_de_baja','asignacion_de_equipos',)
    list_editable = ('status_baja',)
    

    def account_actions(self, obj):
        return format_html(
               '<a class="button" href="{}">Imprimir</a>&nbsp;' 

            )
        account_actions.short_description = 'Account Actions'
        account_actions.allow_tags = True


    def save_model(self, request, obj, form, change):
        equipos_baja = obj.asignacion_de_equipos
        equipos_baja.status = False
        equipos_baja.status_del_equipo_id = 3
        equipos_baja.save()  
        super().save_model(request, obj, form, change)

        # metodo para crear boton de impresion 



    # def account_actions(self, obj):
    #     return format_html(
    #            '<a class="button" href="{}">Imprimir</a>&nbsp;' 

    #         )
    #     account_actions.short_description = 'Account Actions'
    #     account_actions.allow_tags = True

admin.site.register(Datos_Baja,AsignacionDeEquipoAdmin)