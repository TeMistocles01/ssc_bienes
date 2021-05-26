

from Asignar_Equipos.models import AsignacionDeEquipo
from Altas_Equipos_Y_Componentes.models import EquipoYArticulos
from django.forms import ModelForm

class CreationForm(ModelForm):
    class Meta:
        model = AsignacionDeEquipo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
        self.fields['asignacion_de_equipos'].queryset = EquipoYArticulos.objects.filter(status=True)


    

    