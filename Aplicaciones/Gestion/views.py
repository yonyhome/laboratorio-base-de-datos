from django.shortcuts import render,redirect
from .models import Padre,Hijo
from .forms import PadreForm

def inicio(request):
    Padres = Padre.objects.all()   #select * from persona
    contexto =  {
        'Padres':Padres
    }
    return render(request,'padre.html', contexto)

def menu(request):
    return render (request, 'menu.html')

def crearPadre(request):
    if request.method =='GET':
        form = PadreForm()
        contexto = {
        'form':form
        }
    else:
        form = PadreForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('padre')
    return render(request,'crear_Padre.html', contexto)

def editarpadre(request,id):
    padre = Padre.objects.get(id = id)
    if request.method =='GET':
        form = PadreForm(instance = padre)
        contexto = {
            'form':form
        }
    else:
        form =PadreForm(request.POST,instance = padre)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('padre')
    return render(request,'crear_padre.html',contexto)

def eliminarpadre(request,id):
    padre = Padre.objects.get(id = id)
    padre.delete()
    return redirect('padre')