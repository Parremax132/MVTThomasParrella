from django.urls import path
from .views import inicio, plantilla, desafio, listado_fam

urlpatterns = [
    path('', inicio),
    path('template/', plantilla),
    path('desafio/<name>/<age>', desafio),
    path('listado/', listado_fam )
]