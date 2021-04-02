from django import forms
from .models import Padre,Hijo

class PadreForm(forms.ModelForm):
    class Meta:
        model = Padre
        fields = ('id','nom')

class HijoForm(forms.ModelForm):
    class Meta:
        model = Hijo
        #fields = ('id','nom','hijode')
        fields = '__all__'

