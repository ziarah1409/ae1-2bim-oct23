from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from informacion.models import *

# Create your views here.

def listarPaises(request):
    """
        Listar los registros del modelo Equipo,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # equipos
    paises = Pais.objects.all()
    # se obtiene el número de elementos de la lista
    numero_paises = len(paises)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'paises': paises, 'numero_paises': numero_paises}
    return render(request, 'listar_paises.html', informacion_template)

def listarBarrios(request):
    """
        Listar los registros del modelo Equipo,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # equipos
    barrios = Barrio.objects.all()
    # se obtiene el número de elementos de la lista
    numero_barrios = len(barrios)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'barrios': barrios, 'numero_barrios': numero_barrios}
    return render(request, 'listar_barrios.html', informacion_template)