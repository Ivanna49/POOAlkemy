from django.contrib import admin
from django.urls import path
from compra import views

urlpatterns = [
    path('', views.index, name="index") ,
    path('productos/', views.listar_productos, name='listar_productos'),
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('borrar_producto/<int:pk>/', views.borrar_producto, name='borrar_producto'),
    path('editar_proveedor/<int:pk>', views.editar_proveedor, name='editar_proveedor'),
    path('borrar_proveedor/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),
    
]

