from django.db import models

# Create your models here.
# Create your models here.
from datetime import datetime
# Create your models here.
from catalogos.models import CataOficio,CataIDE,CataDireccion,CataTelefono,CataExtencion,CataAdscripcion,CataCargo,CataTicket,ResponsableArea,ResponsableEquipo

from Altas_Equipos_Y_Componentes.models import EquipoYArticulos
class AsignacionDeEquipo(models.Model):
    IDE = models.AutoField(primary_key=True)
    fecha_de_asignacion = models.DateTimeField(default=datetime.now, blank=False, null=False, verbose_name='Fecha:')
    ticket = models.ForeignKey(CataTicket,on_delete= models.SET_NULL,null=True)
    oficio =models.ForeignKey(CataOficio,on_delete= models.SET_NULL,null=True)
     
    
    Registro_responsable_del_area = models.ForeignKey(ResponsableArea,on_delete= models.SET_NULL,null=True, verbose_name='Jefe/Mando responsable de area')
    
    nombre_responsable = models.CharField('Nombre responsable',max_length=255,blank=False, null=False)
    numero_de_empleado = models.CharField('No de empleado responsable',max_length=100,blank=False, null=False)
    
    datos_generales =models.ForeignKey(ResponsableEquipo, on_delete= models.SET_NULL,null=True,verbose_name = 'Datos generales respons')
    
    status_responsable = models.BooleanField('Activo', default=False,null=False,blank=False)

    # USUARIO                                       GRUPO
    asignacion_de_equipos = models.ManyToManyField(EquipoYArticulos)
    
    observaciones = models.TextField('Observaciones',max_length=255, blank=True, null=True)

    class Meta:
        verbose_name='Equipos asignados'
        verbose_name_plural='Equipos asignados'
       
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.nombre_responsable = (self.nombre_responsable).upper()
        self.numero_de_empleado = (self.numero_de_empleado).upper()
        return super(AsignacionDeEquipo, self).save(*args, **kwargs)

    


    

    def __str__(self):
         return '%s %s %s %s %s'%(self.IDE,self.nombre_responsable, self.numero_de_empleado, self.status_responsable, self.asignacion_de_equipos)


