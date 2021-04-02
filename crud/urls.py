"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Aplicaciones.Gestion.views import inicio,crearPadre,editarpadre,eliminarpadre,menu,crearHijo,editarHijo,eliminarHijo,hijo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('padre/',inicio, name= 'padre'),
    path('',menu, name= 'menu'),
    path('crear_padre/',crearPadre,name = 'crear_padre'),
    path('editar_padre/<int:id>/',editarpadre,name = 'editar_padre'),
    path('eliminar_padre/<int:id>/',eliminarpadre, name = 'eliminar_padre'),
    path('hijo/',hijo,name='hijo'),
    path('crear_hijo/',crearHijo,name = 'crear_hijo'),
    path('editar_hijo/<int:id>/',editarHijo,name = 'editar_hijo'),
    path('eliminar_hijo/<int:id>/',eliminarHijo,name = 'eliminar_hijo')
]
