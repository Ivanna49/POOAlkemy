from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def contar(request):
    
    hobbies_adquiridos = [
        {"titulo": "Futbol", "descripcion": "Pelota"},
        {"titulo": "Voley", "descripcion": "Red"},
        {"titulo": "Ajedrez", "descripcion": "Reina"},
        {"titulo": "Paddle", "descripcion": "Paleta"},
    ]

   
    doc_externo = open("C:/Users/ivaba/clase12/miApp/templates/presentacion.html")
    
   
    nombre = "Juancito"

  
    plantilla = Template(doc_externo.read())
    
  
    doc_externo.close()

 
    contexto = Context({"nombre_usuario": nombre, "hobbies" : hobbies_adquiridos})

   
    return HttpResponse(plantilla.render(contexto))