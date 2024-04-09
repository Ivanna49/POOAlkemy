from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto, Proveedor
from .forms import ProveedorForm, ProductoForm

def index(request):
    return render(request, 'index.html')


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})


def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form})


def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()  
        return redirect('listar_proveedores')
    return render(request, 'borrar_proveedor.html', {'proveedor': proveedor})


def agregar_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})


def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()  
        return redirect('listar_productos')
    return render(request, 'borrar_producto.html', {'producto': producto})
