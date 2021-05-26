from django.contrib import admin


# Register your models here.
from .models import EquipoYArticulos,MemoriaRam,DiscoDuro
from .form import CreationForm


    


class DiscoDuroAdmin(admin.ModelAdmin):
    
    
    
    list_display = ('Serie','Modelo','Marca','capacidad_de_disco','tipo_de_disco','status')
    list_filter = ('Serie','Modelo','Marca','capacidad_de_disco','status') 

class MemoriaRamAdmin(admin.ModelAdmin):
    
    
    list_display = ('Serie','Modelo','Marca','capacidad_ram','tipo_de_memoria','status')
    list_filter = ('Serie','Modelo','Marca','capacidad_ram','status') 



class EquipoYArticulosAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):

        if not obj:
            kwargs['form'] = CreationForm
        else:
            pass
            # kwargs['form'] = CreationForm
        return super().get_form(request, obj, **kwargs)
    
    list_filter = ('asigne_equipo','serie','modelo','marca','asignar_pulgadas_pantalla','status_del_equipo','status',)
    list_display = ('asigne_equipo','serie','modelo','marca','discos','memorias_rams','status_del_equipo','status',) 
    #list_editable = ('status_del_equipo',)

    def discos(self, obj):
        
        return ', '.join([str(p) for p in obj.asignar_disco.all()])

    def memorias_rams(self, obj):
        
        return ', '.join([str(p) for p in obj.asignar_memoria.all()])


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        
    #salva los elelementos relacionados aqui guarda varios elementos del ManyToMany  
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        
        obj = form.instance
        discos = obj.asignar_disco.all()
        for disco in discos:
            disco.status = False
            disco.save()
        obj = form.instance
        memoerias = obj.asignar_memoria.all()
        for memoria in memoerias:
            memoria.status = False
            memoria.save()
 


admin.site.register(EquipoYArticulos,EquipoYArticulosAdmin)
admin.site.register(MemoriaRam,MemoriaRamAdmin)
admin.site.register(DiscoDuro,DiscoDuroAdmin)
