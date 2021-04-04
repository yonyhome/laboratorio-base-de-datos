from django.shortcuts import render,redirect
from .models import Padre,Hijo
from .forms import PadreForm,HijoForm
from django.db.models import Count

def inicio(request):
    Padres = Padre.objects.all().order_by('id')  #select * from persona
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
    Hijos = Hijo.objects.all().order_by('id')
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
    form = PadreForm(instance=padre)
    if request.method =='POST':
        form = PadreForm(request.POST, instance=padre)
        if form.is_valid():
            form.save()
            return redirect('padre')
    contexto = {'form':form}
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
    return render(request,'crear_Hijo.html', contexto)
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
    Padres = Padre.objects.all().order_by('id')
    contexto = {
        'Padres':Padres,
        }
    return render(request,'consulta_1.html',contexto)


def cant_hijos(request):
    cantidad = Padre.objects.annotate(num_hijos=Count('hijo')).order_by('id')
    contexto = {
     'cantidad' : cantidad
    }
    return render(request,'consulta_4.html', contexto)

def consulta_padre(request, id):
    hijodepadre = Hijo.objects.filter(hijode__pk = id)
    contexto = {
        'hijodepadre': hijodepadre
    }
    return render(request, 'hijo_de_padre.html', contexto)

def padre_sin_hijo(request):
       #padresolo = Hijo.objects.filter(hijode__pk = p.id)
       #if padresolo == None:

    lista= Padre.objects.filter(hijo__isnull=True).order_by('id')
    contexto = {
        'lista': lista
    }
    return render(request, 'consulta_2.html', contexto)

def hijo_sin_padre(request):
    #hijosolo = Hijo.objects.filter(hijode__pk,null=True)
    hijosolo= Hijo.objects.filter(hijode__pk__isnull = True).order_by('id')
    contexto = {
        'hijosolo': hijosolo
    }
    return render(request, 'consulta_3.html', contexto)





