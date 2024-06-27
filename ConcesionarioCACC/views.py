from django.db import connection
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from ConcesionarioCACC.models import Marcas, Proveedor, Vehiculo
from django.core.files.storage import FileSystemStorage

#region home

def home(request):
    return render(request, "home/home.html")

#endregion

#region marca
def insertarmarca(request):
    if request.method == "POST":
        nombre_marca = request.POST.get('nombre_marca')
        pais_origen = request.POST.get('pais_origen')
        fecha_fundacion = request.POST.get('fecha_fundacion')
        descripcion = request.POST.get('descripcion')
        # Verifica si el estado se proporciona en el formulario
        estado = request.POST.get('estado')
        if estado is None:
            estado = 1  # Asigna el valor predeterminado de 1 si no se proporciona
        
        if nombre_marca and pais_origen and fecha_fundacion and descripcion:
            marcas = Marcas(
                nombre_marca=nombre_marca,
                pais_origen=pais_origen,
                fecha_fundacion=fecha_fundacion,
                descripcion=descripcion,
                estado=estado
            )
            marcas.save()
            return redirect("/marcas/listado")
            
    else:
        return render(request, 'marcas/insertar.html')

def listadomarcas(request):
    marcas = Marcas.objects.filter(estado=1)
    return render(request, 'marcas/listado.html', {'marcas': marcas})

def listadomarcasinactivas(request):
    marcas = Marcas.objects.filter(estado=0)
    return render(request, 'marcas/listadoinactivo.html', {'marcas': marcas})

def inactivarmarca(request,idmarca):
    marcas = connection.cursor()
    marcas.execute("call inactivarmarca('"+str(idmarca)+"')")
    return redirect("/marcas/listado")

def activarmarca(request,idmarca):
    marcas = connection.cursor()
    marcas.execute("call activarmarca('"+str(idmarca)+"')")
    return redirect("/marcas/listado")

def actualizarmarca(request, idmarca):
     if request.method == "POST":
        if request.POST.get('nombre_marca') and request.POST.get('pais_origen') and request.POST.get('fecha_fundacion') and request.POST.get('descripcion'):
            marcas = Marcas.objects.get(id = idmarca)
            marcas.nombre_marca = request.POST.get('nombre_marca')
            marcas.pais_origen = request.POST.get('pais_origen')
            marcas.fecha_fundacion = request.POST.get('fecha_fundacion')
            marcas.descripcion = request.POST.get('descripcion')
            marcas.save()
            return redirect("/marcas/listado")
            
     else:
         marcas = Marcas.objects.filter(id = idmarca)
         return render(request, 'marcas/actualizar.html', {'marcas':marcas})

#endregion

#region proveedor
def insertarproveedor(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        celular = request.POST.get('celular')
        pais = request.POST.get('pais')
        # Verifica si el estado se proporciona en el formulario
        estado = request.POST.get('estado')
        if estado is None:
            estado = 1  # Asigna el valor predeterminado de 1 si no se proporciona
        
        if nombre and cedula and celular and pais:
            proveedor = Proveedor(
                nombre=nombre,
                cedula=cedula,
                celular=celular,
                pais=pais,
                estado=estado
            )
            proveedor.save()
            return redirect("/proveedor/listado")
            
    else:
        return render(request, 'proveedores/insertar.html')

def listadoproveedor(request):
    proveedor = Proveedor.objects.filter(estado=1)
    return render(request, 'proveedores/listado.html', {'proveedor': proveedor})

def listadoproveedorinactivo(request):
    proveedor = Proveedor.objects.filter(estado=0)
    return render(request, 'proveedores/listadoinactivo.html', {'proveedor': proveedor})

def inactivarproveedor(request,idproveedor):
    proveedor = connection.cursor()
    proveedor.execute("call inactivarproveedor('"+str(idproveedor)+"')")
    return redirect("/proveedor/listado")

def activarproveedor(request,idproveedor):
    proveedor = connection.cursor()
    proveedor.execute("call activarproveedor('"+str(idproveedor)+"')")
    return redirect("/proveedor/listado")

def actualizarproveedor(request, idproveedor):
     if request.method == "POST":
        if request.POST.get('nombre') and request.POST.get('cedula') and request.POST.get('celular') and request.POST.get('pais'):
            proveedor = Proveedor.objects.get(id = idproveedor)
            proveedor.nombre = request.POST.get('nombre')
            proveedor.cedula = request.POST.get('cedula')
            proveedor.celular = request.POST.get('celular')
            proveedor.pais = request.POST.get('pais')
            proveedor.save()
            return redirect("/proveedor/listado")
            
     else:
         proveedor = Proveedor.objects.filter(id = idproveedor)
         return render(request, 'proveedores/actualizar.html', {'proveedor':proveedor})
#endregion


#region vehiculo
def insertarvehiculo(request):
    if request.method == "POST":
        if request.POST.get('nombre') and request.POST.get('color') and request.POST.get('modelo') and request.POST.get('capacidad') and request.POST.get('cilindraje') and request.POST.get('cantidad_de_vehiculos') and request.POST.get('precio') and request.FILES['foto'] and request.POST.get('proveedor') and request.POST.get('marcas'):
            producto = Vehiculo()
            producto.nombre = request.POST.get('nombre')
            producto.color = request.POST.get('color')
            producto.modelo = request.POST.get('modelo')
            producto.capacidad = request.POST.get('capacidad')
            producto.cilindraje = request.POST.get('cilindraje')
            producto.cantidad_de_vehiculos = request.POST.get('cantidad_de_vehiculos')
            producto.precio = request.POST.get('precio')
            producto.foto = request.FILES['foto']
            producto.Proveedor = request.POST.get('proveedor')
            producto.Proveedor = Proveedor.objects.get(id=request.POST.get("proveedor"))
            producto.marca = request.POST.get('marcas')
            producto.marca = Marcas.objects.get(id=request.POST.get("marcas"))
            producto.estado = request.POST.get('estado')
            imagen = FileSystemStorage()
            imagen.save(producto.foto.name,producto.foto)
            insertar = connection.cursor()
            insertar.execute("call insertarvehiculo('"+str(producto.nombre)+"','"+str(producto.color)+"','"+str(producto.modelo)+"','"+str(producto.capacidad)+"','"+str(producto.cilindraje)+"','"+str(producto.cantidad_de_vehiculos)+"','"+str(producto.precio)+"','"+str(producto.foto.name)+"','"+str(request.POST.get('proveedor'))+"','"+str(request.POST.get('marcas'))+"','"+str(producto.estado)+"')")
            return redirect("/vehiculo/listado")

    else:
        proveedor = Proveedor.objects.filter(estado=1)
        marcas = Marcas.objects.filter(estado=1)
        return render(request, 'vehiculos/insertar.html', {'proveedor': proveedor, 'marcas': marcas})


    
def listadovehiculo(request):
    vehiculo = Vehiculo.objects.filter(estado=1)
    return render(request, 'vehiculos/listado.html', {'vehiculo': vehiculo})

def listadovehiculoinactivo(request):
    vehiculo = Vehiculo.objects.filter(estado=0)
    return render(request, 'vehiculos/listadoinactivo.html', {'vehiculo': vehiculo})

def inactivarvehiculo(request,idvehiculo):
    vehiculo = connection.cursor()
    vehiculo.execute("call inactivarvehiculo('"+str(idvehiculo)+"')")
    return redirect("/vehiculo/listado")

def activarvehiculo(request,idvehiculo):
    vehiculo = connection.cursor()
    vehiculo.execute("call activarvehiculo('"+str(idvehiculo)+"')")
    return redirect("/vehiculo/listado")


def actualizarvehiculo(request,idvehiculo):
    if request.method == "POST":
        if request.POST.get('nombre') and request.POST.get('color') and request.POST.get('modelo') and request.POST.get('capacidad') and request.POST.get('cilindraje') and request.POST.get('cantidad_de_vehiculos') and request.POST.get('precio') and request.POST.get('proveedor') and request.POST.get('marcas'):
            producto = Vehiculo()
            producto.nombre = request.POST.get('nombre')
            producto.color = request.POST.get('color')
            producto.modelo = request.POST.get('modelo')
            producto.capacidad = request.POST.get('capacidad')
            producto.cilindraje = request.POST.get('cilindraje')
            producto.cantidad_de_vehiculos = request.POST.get('cantidad_de_vehiculos')
            producto.precio = request.POST.get('precio')
            try:
                if request.FILES['foto']:
                    unproducto = Vehiculo.objects.get(id=idvehiculo)
                    fs = FileSystemStorage()
                    fs.delete(unproducto.foto)
                    producto.foto = request.FILES['foto']
                    fs.save(producto.foto.name,producto.foto)
            except:
                print()

            producto.Proveedor = request.POST.get('proveedor')
            producto.Proveedor = Proveedor.objects.get(id=request.POST.get("proveedor"))
            producto.marca = request.POST.get('marcas')
            producto.marca = Marcas.objects.get(id=request.POST.get("marcas"))
            producto.estado = request.POST.get('estado')
            insertar = connection.cursor()
            insertar.execute("call actualizarvehiculo('"+str(idvehiculo)+"','"+str(producto.nombre)+"','"+str(producto.color)+"','"+str(producto.modelo)+"','"+str(producto.capacidad)+"','"+str(producto.cilindraje)+"','"+str(producto.cantidad_de_vehiculos)+"','"+str(producto.precio)+"','"+str(producto.foto.name)+"','"+str(request.POST.get('proveedor'))+"','"+str(request.POST.get('marcas'))+"')")
            return redirect("/vehiculo/listado")

    else:
        proveedor = Proveedor.objects.filter(estado=1)
        marcas = Marcas.objects.filter(estado=1)
        producto = Vehiculo.objects.filter(id=idvehiculo)
        return render(request, 'vehiculos/actualizar.html', {'proveedor': proveedor, 'marcas': marcas, 'vehiculo':producto})



#endregion