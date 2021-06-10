from django.db import models
from datetime import datetime
# Create your models here.
from catalogos.models import CataCargoBaja, CataTelefono,CataExtencion,CataTicketBaja,CataPeriodo,CataStatusBaja,CataAdscripcion
from Asignar_Equipos.models import EquipoYArticulos


# Create your models here.
class Datos_Baja(models.Model):  
    Folio = models.AutoField(primary_key=True)
    status_baja = models.ForeignKey(CataStatusBaja, on_delete= models.SET_NULL,null=True)
    fecha_de_baja = models.DateTimeField(default=datetime.now, blank=False, null=False, verbose_name='Fecha')
    Oficio =models.CharField('Oficio',max_length=255, blank=False, null=False)
    ticket_baja = models.ForeignKey(CataTicketBaja,on_delete= models.SET_NULL,null=True)
    usuario =models.CharField('Usuario',max_length=255, blank=False, null=False)
    cargo =models.ForeignKey(CataCargoBaja,on_delete= models.SET_NULL,null=True)
    Adscripcion =models.ForeignKey(CataAdscripcion,on_delete= models.SET_NULL,null=True)
    telefono =models.ForeignKey(CataTelefono,on_delete= models.SET_NULL,null=True)
    extencion_del_area =models.ForeignKey(CataExtencion, on_delete= models.SET_NULL,null=True)
    asignacion_de_equipos = models.ForeignKey(EquipoYArticulos, on_delete= models.SET_NULL,null=True, verbose_name='Equipo para baja:')
    periodo = models.ForeignKey(CataPeriodo, on_delete= models.SET_NULL,null=True)
    tecico_diacnosticador =models.CharField('Tecnico diacnosticador',max_length=255, blank=False, null=False)
    diagnostico = models.TextField('Diagnóstico',max_length=255, blank=True, null=True)
    class Meta:
        verbose_name='Datos_Baja'
        verbose_name_plural='Datos_Baja'

    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.usuario = (self.usuario).upper()
        self.diagnostico = (self.diagnostico).upper()
        self.tecico_diacnosticador = (self.tecico_diacnosticador).upper()
       
        return super(Datos_Baja, self).save(*args, **kwargs)


    def __str__(self):
        return 'Folio %s %s %s %s %s %s %s %s %s '%(self.Folio,self.fecha_de_baja,self.ticket_baja,self.usuario,self.cargo,self.telefono,self.extencion_del_area,self.asignacion_de_equipos,self.diagnostico)

      