

from django.contrib import admin

# Register your models here.
from .models import AsignacionDeEquipo
from .form import CreationForm


# Register your models here.
# Realiza filtrado de equipos disponible mostrando en el campo solo los disponibles
class AsignacionDeEquipoAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):

        if not obj:
            kwargs['form'] = CreationForm
        else:
            pass
            # kwargs['form'] = CreationForm
        return super().get_form(request, obj, **kwargs)


# class AsignacionDeEquipoAdmin(admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):

#         if not obj:
#             kwargs['form'] = CreationForm
#         else:
#             pass
#             # kwargs['form'] = CreationForm
#         return super().get_form(request, obj, **kwargs)




    # ingresar marca
    search_fields = ['nombre_responsable','numero_de_empleado']
    list_display = ('IDE','nombre_responsable','status_responsable','numero_de_empleado','equipos_y_aditamentos',) 
    #list_editable = ('asignacion_de_equipos',)
    
    def equipos_y_aditamentos(self, obj):
        
        return ', / '.join([str(p) for p in obj.asignacion_de_equipos.all()])

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        
    #salva los elelementos relacionados aqui guarda varios elementos del ManyToMany  
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)



        
        obj = form.instance
        equipos = obj.asignacion_de_equipos.all()
        
        for equipo in equipos:
            equipo.status = False
            equipo.save()


    




admin.site.register(AsignacionDeEquipo,AsignacionDeEquipoAdmin)


    
