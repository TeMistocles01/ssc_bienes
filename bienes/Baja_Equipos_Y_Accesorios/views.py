
from django.shortcuts import render,HttpResponse
from Baja_Equipos_Y_Accesorios.models import Datos_Baja


#se importa para definir comoparametro en la clase
from django.views.generic import View
from django.template.loader import get_template


from weasyprint import HTML


class data_baja(View):
    def get(self, requets, *args, **kwargs):
        try:
            template = get_template('dictamen.html')
            context = {
                 'baja': Datos_Baja.objects.get(pk=self.kwargs['pk'])
             }
            html = template.render(context)

            pdf = HTML(string=html,base_url=requets.build_absolute_uri()).write_pdf()
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass