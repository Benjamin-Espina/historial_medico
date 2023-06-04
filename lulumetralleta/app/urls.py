from django.urls import path
from .views import home, cita, informacion, medicos

urlpatterns = [
    path('', home, name="home"),
    path('cita/', cita, name="cita"),
    path('informacion/', informacion, name="informacion"),
    path('medicos/', medicos, name='medicos')
]
