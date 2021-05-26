


from Altas_Equipos_Y_Componentes.models import DiscoDuro, EquipoYArticulos, MemoriaRam
from django.forms import ModelForm

class CreationForm(ModelForm):
    class Meta:
        model = EquipoYArticulos
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
        self.fields['asignar_disco'].queryset = DiscoDuro.objects.filter(status=True)
        self.fields['asignar_memoria'].queryset = MemoriaRam.objects.filter(status=True)


    