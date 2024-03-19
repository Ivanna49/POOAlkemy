from urllib import request
from django.shortcuts import render
from .models import Estudiante

def crear_estudiante(request):
    nuevo_estudiante = Estudiante.objects.create(
        nombre = "Sharon", 
        apellido = "Stone", 
        edad = 20, 
        nota = 9.3
        )
   
    
    return render(     
           request, 'nuevo_estudiante.html',
           {'nuevo_estudiante': nuevo_estudiante}
           )
        
def mostrar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes}
                  )
    
    
def filtrar_estudiantes_edad(request, edad):
    studentEncontrado = Estudiante.objects.filter(edad = edad)
    return render(request, 'estudiante_filtrados.html', {'studentEncontrado': studentEncontrado}
                  )
   
   
def update_estudiante_id(request, id):
    studentActualizar = Estudiante.objects.get(id = id)
    studentActualizar. nombre = 'Sharon'
    studentActualizar. apellido = 'Stone'
    studentActualizar. edad = '20'
    studentActualizar. nota = 9.30 
    studentActualizar. save()
    return render(request, 'estudiante_actualizado.html', {'studentActualizar': studentActualizar}
                    )
                  
                  
                     
def delete_estudiante_id(request, id):
    studentABorrar = Estudiante.objects.get(id = id)
    studentABorrar.delete()
    estudiantes = Estudiante.objects.all ()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes}
                    )
    
    
                 
def delete_all(request):
    estudiantes = Estudiante.objects.all()
    estudiantes.delete()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes}
                    )