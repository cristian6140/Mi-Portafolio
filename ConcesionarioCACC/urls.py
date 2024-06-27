"""
URL configuration for ConcesionarioCACC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ConcesionarioCACC.views import home, insertarmarca, listadomarcas, listadomarcasinactivas, inactivarmarca, activarmarca, actualizarmarca, insertarproveedor, listadoproveedor, listadoproveedorinactivo, inactivarproveedor, activarproveedor, actualizarproveedor, insertarvehiculo, listadovehiculo, listadovehiculoinactivo, inactivarvehiculo, activarvehiculo, actualizarvehiculo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('marcas/insertar', insertarmarca), #marcas
    path('marcas/listado', listadomarcas),
    path('marcas/listadoinactivo', listadomarcasinactivas),
    path('marcas/inactivar/<int:idmarca>', inactivarmarca),
    path('marcas/activar/<int:idmarca>', activarmarca),
    path('marcas/actualizar/<int:idmarca>', actualizarmarca),
    path('proveedor/insertar', insertarproveedor), #proveedores
    path('proveedor/listado', listadoproveedor),
    path('proveedor/listadoinactivo', listadoproveedorinactivo),
    path('proveedor/inactivar/<int:idproveedor>', inactivarproveedor),
    path('proveedor/activar/<int:idproveedor>', activarproveedor),
    path('proveedor/actualizar/<int:idproveedor>', actualizarproveedor),
    path('vehiculo/insertar', insertarvehiculo), #vehiculos
    path('vehiculo/listado', listadovehiculo),
    path('vehiculo/listadoinactivo', listadovehiculoinactivo),
    path('vehiculo/inactivar/<int:idvehiculo>', inactivarvehiculo),
    path('vehiculo/activar/<int:idvehiculo>', activarvehiculo),
    path('vehiculo/actualizar/<int:idvehiculo>', actualizarvehiculo),
]
