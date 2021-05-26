from django.db import models

# Create your models here.
class Catapulgadas(models.Model):
    pulgadas = models.CharField('Pulgadas',max_length=100, blank=True, null=True)
    class Meta:
        verbose_name='Catálogo pulgadas'
        verbose_name_plural='Catálogo pulgadas'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.pulgadas = (self.pulgadas).upper()
        
        
        return super(Catapulgadas, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.pulgadas)

class CataProcesador(models.Model):
    procesador = models.CharField('Pulgadas',max_length=100, blank=True, null=True)
    class Meta:
        verbose_name='Catálogo procesador'
        verbose_name_plural='Catálogo procesador'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.procesador = (self.procesador).upper()
        
        
        return super(CataProcesador, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.procesador)
class CataEquipoArticulos(models.Model):
    forma_de_adquisicion = models.CharField('Forma de adquisición:',max_length=100, blank=False, null=False)
    class Meta:
        verbose_name='Catálogo Equipos y aditamentos'
        verbose_name_plural='Catálogo Equipos y aditamentos'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.forma_de_adquisicion = (self.forma_de_adquisicion).upper()
        
        
        return super(CataEquipoArticulos, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.forma_de_adquisicion)

class CataFormAdqui(models.Model):
    forma_de_adquisicion = models.CharField('Forma de adquisición:',max_length=100, blank=False, null=False)
    class Meta:
        verbose_name='Catálogo forma de adquisición'
        verbose_name_plural='Catálogo forma de adquisición'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.forma_de_adquisicion = (self.forma_de_adquisicion).upper()
        
        
        return super(CataFormAdqui, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.forma_de_adquisicion)
class CataNumContra(models.Model):
    contrato_numero = models.CharField('Número',max_length=255, blank=False, null=False)
    class Meta:
        verbose_name='Catálogo número de contrato'
        verbose_name_plural='Catálogo número de contrato'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.contrato_numero = (self.contrato_numero).upper()
        
        
        return super(CataNumContra, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.contrato_numero)

class CataNuevoReuso(models.Model):
    registro_componente = models.CharField('Asigne: Nuevo/Reuso',max_length=30, blank=False, null=False)
    class Meta:
        verbose_name='Catálogo nuevo/Reuso'
        verbose_name_plural='Catálogo Nuevo/Reuso'

    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.registro_componente = (self.registro_componente).upper()
        
        
        return super(CataNuevoReuso, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.registro_componente)
 

class CataStatus(models.Model):

    status_del_equipo = models.CharField('Status del equipo:',max_length=50, blank=False, null=False)
    class Meta:
        #asigna nombre a la tabla
        verbose_name='Catálogo status del equipo'
        #asigna nombre de la lista de entrada (modelos de la aplicasión)
        verbose_name_plural='Catálogo status del equipo'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.status_del_equipo = (self.status_del_equipo).upper()
        
        
        return super(CataStatus, self).save(*args, **kwargs)
        
    #muestra como se mostrara la vista en el formato de salida en lalista
    def __str__(self):
        return '%s'%(self.status_del_equipo)
class CataTipoRegist(models.Model):
    tipo_de_registro = models.CharField('Consumible/',max_length=30, blank=False, null=False)
    
    class Meta:
        #asigna nombre a la tabla
        verbose_name='Catálogo tipo de registro equipo'
        #asigna nombre de la lista de entrada (modelos de la aplicasión)
        verbose_name_plural='Catálogo de tipo registro equipo'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.tipo_de_registro = (self.tipo_de_registro).upper()
        
        
        return super(CataTipoRegist, self).save(*args, **kwargs)
        
    #muestra como se mostrara la vista en el formato de salida en lalista
    def __str__(self):
        return '%s'%(self.tipo_de_registro)

class CataColores(models.Model):
    color = models.CharField('Color',max_length=30, blank=True, null=True)

    class Meta:

        #asigna nombre a la tabla
        verbose_name='Catálogo Colores'
        #asigna nombre de la lista de entrada (modelos de la aplicasión)
        verbose_name_plural='Catálogo Colores'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):

        self.color = (self.color).upper()
        return super(CataColores, self).save(*args, **kwargs)
    
    
        
    #muestra como se mostrara la vista en el formato de salida en lalista
    def __str__(self):
        return '%s'%(self.color)
# catalogo solo para marcas de dico duro y memoria ram
class CataMarcasDM(models.Model):
    
    id = models.AutoField(primary_key=True )
    marca = models.CharField('Asigne nombre de la marca',max_length=30, blank=False, null=False)    
    
    class Meta:
        verbose_name='Catálogo marcas disco y ram'
        verbose_name_plural='Catálogo  marcas disco y ram'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.marca = (self.marca).upper()
        
        
        return super(CataMarcasDM, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.marca)

class CataMarcasEquiTMP(models.Model):
    
    id = models.AutoField(primary_key=True )
    marca = models.CharField('Asigne nombre de la marca',max_length=30, blank=False, null=False)    
    
    class Meta:
        verbose_name='Catálogo marcas equipos y complementos'
        verbose_name_plural='Catálogo marcas equipos y complementos'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.marca = (self.marca).upper()
        
        
        return super(CataMarcasEquiTMP, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.marca)


# catalogos solo memoria ram

class CataTipoDDR(models.Model):

    id = models.AutoField(primary_key=True )
    tipo_de_memoria = models.CharField('Asigne DDR/2/3/4',max_length=30, blank=False, null=False)

    class Meta:
        verbose_name='Catálogo memoria Ram Tipo'
        verbose_name_plural='Catálogo memoria Ram Tipo'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.tipo_de_memoria = (self.tipo_de_memoria).upper()
        
        
        return super(CataTipoDDR, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.tipo_de_memoria)

class CataCapaRam(models.Model):

    id = models.AutoField(primary_key=True )
    capacidad_de_memoria = models.CharField('Asigne capacida Gygabyte',max_length=30, blank=False, null=False)
   
      
    class Meta:
        verbose_name='Catálogo memoria ram capacidad'
        verbose_name_plural='Catálogo memoria ram capacidad'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.capacidad_de_memoria = (self.capacidad_de_memoria).upper()
        
        
        return super(CataCapaRam, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.capacidad_de_memoria)

#  catalogos solo para disco duro

class CataCapaAlmDis(models.Model):

    id = models.AutoField(primary_key=True )    
    disco_capacidad = models.CharField('Asigne capacidad GB/TB',max_length=30, blank=False, null=False)    
    
    class Meta:
        verbose_name='Catálogo capacidad almacenamiento'
        verbose_name_plural='Catálogo capacidad almacenamiento'

    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.disco_capacidad = (self.disco_capacidad).upper()
        
        
        return super(CataCapaAlmDis, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.disco_capacidad)
class CataTipoDis(models.Model):
    tipo_de_disco = models.CharField('Asigne:SSD/HDD',max_length=3, blank=False, null=False)
    
    
    class Meta:
        verbose_name='Catálogo disco tipo'
        verbose_name_plural='Catálogo tipo disco'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.tipo_de_disco = (self.tipo_de_disco).upper()
        
        
        return super(CataTipoDis, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.tipo_de_disco)
class CataVelocDis(models.Model):

    velocidad = models.CharField('Asigne 2.5/3.5',max_length=30, blank=False, null=False)    
    class Meta:
        verbose_name='Catálogo velocidad disco'
        verbose_name_plural='Catálogo velocidad disco'
    # funcion para convertir texto ingresado por teclado en minuscula en mayuscula
    def save(self, *args, **kwargs):
        self.velocidad = (self.velocidad).upper()
        return super(CataVelocDis, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.velocidad)






    
    

    
##############################catalogos modelo asignar equipos y componentes

class CataOficio(models.Model):
    
    oficio = models.CharField('Oficio',max_length=255, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo Oficio'
        verbose_name_plural='Catálogo Oficio'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.oficio = (self.oficio).upper()
        
        return super(CataOficio, self).save(*args, **kwargs)    
            

    def __str__(self):
        return '%s '%(self.oficio)
class CataIDE(models.Model):

    IDE = models.CharField('IDE',max_length=255, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo IDE'
        verbose_name_plural='Catálogo IDE'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.IDE = (self.IDE).upper()
        
        return super(CataIDE, self).save(*args, **kwargs)    

    def __str__(self):
        return '%s '%(self.IDE)

class CataDireccion(models.Model):

    direccion = models.TextField('Dirección',max_length=255, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo dirección'
        verbose_name_plural='Catálogo Dirección'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.direccion = (self.direccion).upper()
        
        return super(CataDireccion, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.direccion)

class CataTelefono(models.Model):

    telefono = models.CharField('Teléfono No',max_length=20, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo teléfono'
        verbose_name_plural='Catálogo Teléfono'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.telefono = (self.telefono).upper()
        
        return super(CataTelefono, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.telefono)
class CataExtencion(models.Model):

    extencion = models.CharField('Extensión',max_length=20, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo extensión'
        verbose_name_plural='Catálogo extensión'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.extencion = (self.extencion).upper()
        
        return super(CataExtencion, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.extencion)

class CataAdscripcion(models.Model):

    adscripccion = models.CharField('Adscripción',max_length=255, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo adscripción'
        verbose_name_plural='Catálogo Adscripción'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.adscripccion = (self.adscripccion).upper()
        
        return super(CataAdscripcion, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.adscripccion)



class ResponsableEquipo(models.Model):
     # datos generales 
    adscripcion =models.ForeignKey(CataAdscripcion, on_delete= models.SET_NULL,null=True)
    telefono_del_area =models.ForeignKey(CataTelefono, on_delete= models.SET_NULL,null=True)
    extencion =models.ForeignKey(CataExtencion, on_delete= models.SET_NULL,null=True)
    direccion = models.ForeignKey(CataDireccion, on_delete= models.SET_NULL,null=True, verbose_name='Ubicación del area')

    class Meta:
        verbose_name='Catálogo Datos generales'
        verbose_name_plural='Catálogo Datos generales'
        
    def __str__(self):
        return '%s'%(self.adscripcion)

class CataCargo(models.Model):
    
    cargo = models.CharField('Cargo',max_length=50, blank=False, null=False) 
    
    class Meta:
        verbose_name='Catálogo cargos'
        verbose_name_plural='Catálogo cargos'

    def save(self, *args, **kwargs):
        self.cargo = (self.cargo).upper()
        return super(CataCargo, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.cargo)

class ResponsableArea(models.Model):
    id = models.AutoField(primary_key=True) 
    
    nombre =models.CharField('Nombre',max_length=255, blank=False, null=False)
    numero_de_empleado =models.CharField('Número de empleado',max_length=20, blank=False, null=False)
    cargo = models.ForeignKey(CataCargo, on_delete= models.SET_NULL,null=True)
    adscripcion =models.ForeignKey(CataAdscripcion,on_delete= models.SET_NULL,null=True)
    telefono_del_area =models.ForeignKey(CataTelefono,on_delete= models.SET_NULL,null=True)
    extencion =models.ForeignKey(CataExtencion,on_delete= models.SET_NULL,null=True)
    direccion = models.ForeignKey(CataDireccion,on_delete= models.SET_NULL,null=True, verbose_name='Ubicación del area')

    class Meta:
        verbose_name='Catálogo Responsable del area'
        verbose_name_plural='Catálogo Responsable del area'

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.numero_de_empleado = (self.numero_de_empleado).upper()
        
        return super(ResponsableArea, self).save(*args, **kwargs)    

    def __str__(self):
        return '%s'%(self.nombre)

class CataAntivirus(models.Model):
    antivirus = models.CharField('Antivirus',max_length=50, blank=False, null=False) 
    
    class Meta:
        verbose_name='Catálogo Antivirus'
        verbose_name_plural='Software Antivirus'

    def save(self, *args, **kwargs):
        self.antivirus = (self.antivirus).upper()
        
        return super(CataAntivirus, self).save(*args, **kwargs)    
    
    def __str__(self):
        return '%s '%(self.antivirus)

class CataOffice(models.Model):

    office = models.CharField('Office',max_length=20, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo Offices'
        verbose_name_plural='Software Offices'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.office = (self.office).upper()
        
        return super(CataOffice, self).save(*args, **kwargs)    
    
    

    def __str__(self):
        return '%s '%(self.office)

class CataSistemaOperativo(models.Model):

    sistema_operativo = models.CharField('Sistema Operativo',max_length=20, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo sistema operativos'
        verbose_name_plural='Catálogo Software Sistema Operativo'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.sistema_operativo = (self.sistema_operativo).upper()
        
        return super(CataSistemaOperativo, self).save(*args, **kwargs)    
        

    def __str__(self):
        return '%s '%(self.sistema_operativo)
 
 # modelos que asignan equipos de computo

class CataTicket(models.Model):

    ticket = models.CharField('Ticket',max_length=20, blank=False, null=False)  
    
    class Meta:
        verbose_name='Catálogo ticket'
        verbose_name_plural='Catálogo Ticket'

    # funcion para comvertir texto minusculas en mayuculas
    def save(self, *args, **kwargs):
        self.ticket = (self.ticket).upper()
        
        return super(CataTicket, self).save(*args, **kwargs) 

    def __str__(self):
        return '%s '%(self.ticket)

class Sofware(models.Model):
    sistema_operativo = models.ForeignKey(CataSistemaOperativo,on_delete= models.SET_NULL,null=True,verbose_name='Sistema Operativo')
    office = models.ForeignKey(CataOffice,on_delete= models.SET_NULL,null=True,verbose_name='Office')
    Antivirus = models.ForeignKey(CataAntivirus,on_delete= models.SET_NULL,null=True,verbose_name='Antivirus')
    
    class Meta:
        verbose_name='Catálogo Software'
        verbose_name_plural='Catálogo Software'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula

    def __str__(self):
        return f'Sistema operativo:{self.sistema_operativo}Office:{self.office}Antivirus:{self.Antivirus}'


class CataCargoBaja(models.Model):
    
    cargo = models.CharField('Cargo',max_length=50, blank=False, null=False) 
    
    class Meta:
        verbose_name='Catálogo cargos'
        verbose_name_plural='Catálogo cargos'

    def save(self, *args, **kwargs):
        self.cargo = (self.cargo).upper()
        return super(CataCargoBaja, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.cargo)

class CataTicketBaja(models.Model):
    
    ticket_baja = models.CharField('N Ticket baja',max_length=50, blank=False, null=False) 
    
    class Meta:
        verbose_name='Catálogo tikect bajas'
        verbose_name_plural='Catálogo tikect bajas'

    def save(self, *args, **kwargs):
        self.ticket_baja = (self.ticket_baja).upper()
        return super(CataTicketBaja, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.ticket_baja)

#catalogos  modulo de bajas 
class CataPeriodo(models.Model):
    
    periodo = models.CharField('Periodo',max_length=50, blank=False, null=False) 
    
    class Meta:
        verbose_name='Catálogo periodo'
        verbose_name_plural='Catálogo periodo'

    def save(self, *args, **kwargs):
        self.periodo = (self.periodo).upper()
        return super(CataPeriodo, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.periodo)

class CataStatusBaja(models.Model):
    
    status_baja = models.CharField('Status',max_length=100, blank=False, null=False) 
    
    class Meta:
        verbose_name='Catálogo status baja'
        verbose_name_plural='Catálogo status baja'

    def save(self, *args, **kwargs):
        self.status_baja = (self.status_baja).upper()
        return super(CataStatusBaja, self).save(*args, **kwargs)

    def __str__(self):
        return '%s '%(self.status_baja)