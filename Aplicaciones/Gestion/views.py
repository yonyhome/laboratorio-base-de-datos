from django.shortcuts import render,redirect
from .models import Padre,Hijo
from .forms import PadreForm,HijoForm

def inicio(request):
    Padres = Padre.objects.all()   #select * from persona
    if request.method =='GET':
        form = PadreForm()
        contexto = {
        'form':form,
        'Padres':Padres,
        }
    else:
        form = PadreForm(request.POST)
        contexto = {
        'form':form,
        'Padres':Padres,
        }
        if form.is_valid():
            form.save()
            return redirect('padre')
    return render(request,'padre.html', contexto)
def hijo(request):
    Hijos = Hijo.objects.all()
    if request.method =='GET':
        form = HijoForm()
        contexto = {
        'form':form,
        'Hijos':Hijos,
        }
    else:
        form = HijoForm(request.POST)
        contexto = {
        'form':form,
        'Hijos':Hijos,
        }
        if form.is_valid():
            form.save()
            return redirect('hijo')
    return render(request,'hijo.html', contexto)

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



def crearHijo(request):
    if request.method =='GET':
        form = HijoForm()
        contexto = {
        'form':form
        }
    else:
        form = HijoForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('hijo')
    return render(request,'crear_Padre.html', contexto)
def editarHijo(request,id):
    hijo = Hijo.objects.get(id = id)
    if request.method =='GET':
        form = HijoForm(instance = hijo)
        contexto = {
            'form':form
        }
    else:
        form =HijoForm(request.POST,instance = hijo)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('hijo')
    return render(request,'crear_hijo.html',contexto)
def eliminarHijo(request, id):
    hijo = Hijo.objects.get(id = id)
    hijo.delete()
    return redirect('hijo')

def consulta_1(request):
    Padres = Padre.objects.all()
    contexto = {
        'Padres':Padres,
        }
    return render(request,'consulta_1.html',contexto)

def consulta_2(request):
    return render(request,'consulta_2.html')

def consulta_3(request):
    return render(request,'consulta_3.html')

def consulta_4(request):
    return render(request,'consulta_4.html')

def consulta_padre(request, id):
    hijodepadre = Hijo.objects.get(id = this.id)
    contexto = {
        'hijodepadre': hijodepadre
    }
    return render(request, 'hijo_de_padre.html', contexto)