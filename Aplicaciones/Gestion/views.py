from django.shortcuts import render,redirect
from .models import Padre,Hijo
from .forms import PadreForm

def inicio(request):
    Padres = Padre.objects.all()   #select * from persona
    contexto =  {
        'Padres':Padres
    }
    return render(request,'index.html', contexto)
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
            return redirect('index')
        
    
    
    return render(request,'crear_Padre.html', contexto)