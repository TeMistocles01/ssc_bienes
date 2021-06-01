from django.db import models

# Create your models here.
from catalogos.models import CataFormAdqui,CataNumContra,CataNuevoReuso,CataMarcasEquiTMP,CataCapaAlmDis,CataTipoDis,CataVelocDis,CataTipoRegist,CataStatus,CataTipoDDR,CataCapaRam,CataEquipoArticulos,CataColores,Catapulgadas,CataMarcasDM,CataProcesador,Sofware



################### Disco duro

class DiscoDuro(models.Model):
    id = models.AutoField(primary_key=True)
    forma_de_adquisicion = models.ForeignKey(CataFormAdqui, on_delete= models.SET_NULL,null=True, verbose_name='Forma de adquisición')
    numero_de_contrato = models.ForeignKey(CataNumContra,  on_delete= models.SET_NULL,null=True, verbose_name='Número de contrato')
    componente_nuevo_reuso = models.ForeignKey(CataNuevoReuso, on_delete= models.SET_NULL,null=True,verbose_name='Estado componente')
    
    Marca = models.ForeignKey(CataMarcasDM,on_delete= models.SET_NULL,null=True)
    
    
    Serie = models.CharField('Serie',max_length=255, blank=False, null=False,unique=True)
    Modelo = models.CharField('Modelo',max_length=255, blank=False, null=False)
    capacidad_de_disco =  models.ForeignKey(CataCapaAlmDis, on_delete= models.SET_NULL,null=True, verbose_name='Capacidad de almacenamiento GB/TB')
    tipo_de_disco =  models.ForeignKey(CataTipoDis, on_delete= models.SET_NULL,null=True, verbose_name='Tipo de disco: SSD/HDD')
    velocidad_disco =models.ForeignKey(CataVelocDis, on_delete= models.SET_NULL,null=True, verbose_name='Tamaño de disco duro')

    tipo_de_registro = models.ForeignKey(CataTipoRegist,on_delete= models.SET_NULL,null=True,verbose_name='Tipo de registro')
    
    status_del_equipo = models.ForeignKey(CataStatus,on_delete= models.SET_NULL,null=True)
    
    status = models.BooleanField('Disponible', default=True)
    
    class Meta:
        verbose_name='Disco Duro'
        verbose_name_plural='Disco Duro'


        
    

    

    def __str__(self):
        return '%s '%(self.Serie)

 
################### Memoria ram
class MemoriaRam(models.Model):
    id = models.AutoField(primary_key=True)
    forma_de_adquisicion = models.ForeignKey(CataFormAdqui, on_delete= models.SET_NULL,null=True, verbose_name='Forma de adquisición')
    numero_de_contrato = models.ForeignKey(CataNumContra, on_delete= models.SET_NULL,null=True, verbose_name='Número de contrato')
    componente_nuevo_reuso = models.ForeignKey(CataNuevoReuso, on_delete= models.SET_NULL,null=True,verbose_name='Estado componente')
   
    Marca = models.ForeignKey(CataMarcasDM, on_delete= models.SET_NULL,null=True,verbose_name='Marca')  
    
    Serie = models.CharField('Serie',max_length=255, blank=False, null=False,unique=True)
    Modelo = models.CharField('Modelo',max_length=255, blank=False, null=False)
    
    tipo_de_memoria = models.ForeignKey(CataTipoDDR,on_delete= models.SET_NULL,null=True, verbose_name='Tipo de memoria DDR/2/3/4')
    capacidad_ram = models.ForeignKey(CataCapaRam, on_delete= models.SET_NULL,null=True,verbose_name='Capacida de memoria GB')
    tipo_de_registro = models.ForeignKey(CataTipoRegist, on_delete= models.SET_NULL,null=True,verbose_name='Tipo de registro')
    status_del_equipo = models.ForeignKey(CataStatus, on_delete= models.SET_NULL,null=True)
    status = models.BooleanField('Disponible', default=True)
    
    class Meta:
        verbose_name='Memoria Ram'
        verbose_name_plural='Memoria Ram'
   

    def __str__(self):
        return '%s'%(self.Serie, )




# class EquipoYArticulosManager(models.Manager):

#     def get_queryset(self ):
#         return super(EquipoYArticulosManager, self).get_queryset().filter(status=True)


        

class EquipoYArticulos(models.Model):

    id = models.AutoField(primary_key=True)
    asigne_equipo = models.ForeignKey(CataEquipoArticulos, on_delete= models.SET_NULL,null=True, verbose_name='Equipo o articulo')
    forma_de_adquisicion = models.ForeignKey(CataFormAdqui, on_delete= models.SET_NULL,null=True, verbose_name='Forma de adquisición')
    numero_de_contrato = models.ForeignKey(CataNumContra, on_delete= models.SET_NULL,null=True, verbose_name='Número de contrato')
    componente_nuevo_reuso = models.ForeignKey(CataNuevoReuso, on_delete= models.SET_NULL,null=True,verbose_name='Estado del equipo/componente')
    clave_cam = models.CharField('Clave cam',max_length=255, blank=False, null=False)
    
    
    asignar_disco = models.ManyToManyField(DiscoDuro,blank=True)
    asignar_memoria = models.ManyToManyField(MemoriaRam,blank=True)
    
    procesador = models.ForeignKey(CataProcesador,on_delete= models.SET_NULL,null=True, blank=True)
    asignar_sofware = models.ForeignKey(Sofware,on_delete= models.SET_NULL,null=True, blank=True)
    asignar_pulgadas_pantalla = models.ForeignKey(Catapulgadas, on_delete= models.SET_NULL,null=True, blank=True,verbose_name='Pulgadas pantalla')
    marca = models.ForeignKey(CataMarcasEquiTMP, on_delete= models.SET_NULL,null=True)
    serie = models.CharField('Serie',max_length=30, blank=False, null=False,unique=True)    
    modelo = models.CharField('Modelo',max_length=30, blank=False, null=False)
   
    
    tipo_de_registro = models.ForeignKey(CataTipoRegist, on_delete= models.SET_NULL,null=True,verbose_name='Tipo de registro')
    status_del_equipo = models.ForeignKey(CataStatus, on_delete= models.SET_NULL,null=True)
    observaciones = models.TextField('Observaciones',max_length=1000, blank=True, null=True)
    status = models.BooleanField('Disponible', default=True)
    
    
    class Meta:
        verbose_name=' Equipos y Articulos'
        verbose_name_plural='Equipos y Articulos'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.serie = (self.serie).upper()
        self.clave_cam = (self.clave_cam).upper()
        self.modelo = (self.modelo).upper()
       
        self.observaciones = (self.observaciones).upper()
        
        return super(EquipoYArticulos, self).save(*args, **kwargs)

    #objects = EquipoYArticulosManager()    
    # elementos visuales en el formulario
    def __str__(self):
        return 'Serie %s'%(self.serie)









