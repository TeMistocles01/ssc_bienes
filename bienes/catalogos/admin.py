from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import CataNuevoReuso, CataStatus, CataTipoRegist, CataMarcasDM, CataTipoDDR, CataCapaRam, CataCapaAlmDis, CataTipoDis, CataVelocDis,CataFormAdqui,CataNumContra, CataMarcasEquiTMP,CataEquipoArticulos,CataColores,Catapulgadas,CataProcesador,CataOficio,CataIDE,CataDireccion,CataTelefono,CataExtencion,CataTicket,CataSistemaOperativo,CataOffice,CataAntivirus,CataCargo,CataAdscripcion, Sofware,CataCargoBaja, CataTicketBaja,ResponsableArea,ResponsableEquipo,CataPeriodo,CataStatusBaja

admin.site.register(CataNuevoReuso)
admin.site.register(CataStatus)
admin.site.register(CataTipoRegist)
admin.site.register(CataMarcasDM)
admin.site.register(CataTipoDDR)
admin.site.register(CataCapaRam)
admin.site.register(CataCapaAlmDis)
admin.site.register(CataFormAdqui)
admin.site.register(CataNumContra)
admin.site.register(CataMarcasEquiTMP)


admin.site.register(CataVelocDis)
admin.site.register(CataTipoDis)


admin.site.register(CataEquipoArticulos)
admin.site.register(CataColores)
admin.site.register(Catapulgadas)
admin.site.register(CataProcesador)
admin.site.register(Sofware)
# asignar equipos
admin.site.register(CataOficio)
admin.site.register(CataIDE)
admin.site.register(CataDireccion)
admin.site.register(CataTelefono)

admin.site.register(CataExtencion)
admin.site.register(CataAdscripcion)
admin.site.register(ResponsableArea)

admin.site.register(ResponsableEquipo)

admin.site.register(CataCargo)




admin.site.register(CataAntivirus)
admin.site.register(CataOffice)
admin.site.register(CataSistemaOperativo)

admin.site.register(CataTicket)

admin.site.register(CataCargoBaja)

admin.site.register(CataTicketBaja)

#moduo de baja

admin.site.register(CataPeriodo)
admin.site.register(CataStatusBaja)

