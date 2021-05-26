from django.urls import path

# para vistas por clase
from Baja_Equipos_Y_Accesorios.views import data_baja

urlpatterns = [


    path('Dictamen/<int:pk>/', data_baja.as_view()),
    
   

]