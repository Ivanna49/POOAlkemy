from django.urls import path
from . import views


urlpatterns = [
    path('', views.mostrar_estudiantes),
    path('create', views.crear_estudiante),
    path('filter/<int:edad>', views.filtrar_estudiantes_edad),
    path('update/<int:id>', views.update_estudiante_id),
    path('delete/<int:id>', views.delete_estudiante_id),
    path('delete', views.delete_all),
    ]