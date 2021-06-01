from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Datos_Baja


# Register your models here.
class AsignacionDeEquipoAdmin(admin.ModelAdmin):
    
    
    
    list_display = ('Folio','fecha_de_baja','status_baja','Oficio','ticket_baja','asignacion_de_equipos','diagnostico',) 
    list_filter= ('status_baja','Oficio','periodo','ticket_baja','fecha_de_baja','asignacion_de_equipos',)
    list_editable = ('status_baja',)

    def save_model(self, request, obj, form, change):
        equipos_baja = obj.asignacion_de_equipos
        equipos_baja.status = False
        equipos_baja.save()  
        super().save_model(request, obj, form, change)

    
    
 





admin.site.register(Datos_Baja,AsignacionDeEquipoAdmin)