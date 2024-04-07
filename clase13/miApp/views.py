from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

def mostrarTemplate(request):
    ruta =  "C:/Users/ivaba/ALKEMY/clase13/miApp/templates/index.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close
    contexto = Context()
    return HttpResponse(plantilla.render(contexto))


    
