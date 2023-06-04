from django.urls import path
from .views import home, cita
urlpatterns = [
    path('', home, name="home"),
    path('cita/', cita, name="cita")
]
